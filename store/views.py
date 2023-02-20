from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.generic import DetailView
from django.contrib import messages
import json
import stripe
import datetime
from .models import *
from .forms import CommentForm


def item_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, "store/item_list.html", context)


def item_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    comments = Comment.objects.filter(product=product, approved=True)
    form = CommentForm(request.POST or None)
    context = {
        'product': product,
        'comments': comments,
        "form": form,
    }
    return render(request, "store/item_view.html", context)


def add_comment(request, product_id):
    """
    Function for user to add comments
    """
    product = get_object_or_404(Product, id=product_id)
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save(commit=False)
            form.instance.recipe = product
            form.instance.user = request.user
            form.save()
            messages.success(request, "Your comment is pending approval!")
            return redirect(item_view, product_id)


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,
                                                     complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {
        'items': items,
        'order': order
    }
    return render(request, "store/cart.html", context)


def checkout(request):
    # pub_key = settings.STRIPE_API_KEY_PUBLISHABLE
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,
                                                     complete=False)
        order.shipping = True
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {
        'items': items,
        'order': order
    }
    return render(request, "store/checkout.html",
                  context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action', action)
    print('productId', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer,
                                                 complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order,
                                                         product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    print('Data:', request.body)
    print(request.user.customer, 'user')
    print(request.user.email, 'email')
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,
                                                     complete=False)
        print(order, 'orderItem')
        total = float(data['form']['total'])
        order.transaction_id = transaction_id
        order.shipping = True

        if total == order.get_cart_total:
            order.complete = True
        order.save()
        print(order.shipping)

        if order.shipping is True:
            ShippingAddress.objects.create(
                    customer=customer,
                    order=order,
                    address=data['shipping']['address'],
                    city=data['shipping']['city'],
                    postcode=data['shipping']['postcode'],
                    county=data['shipping']['country'],

            )

    else:
        print('User is not logged in')
    return JsonResponse('Payment complete!', safe=False)
