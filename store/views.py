from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import JsonResponse
from django.views.generic import DetailView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import datetime
from django.db.models.functions import Lower

from .models import *
from .forms import CommentForm, ProductForm


def item_list(request):
    """ A view to render the Prodcuts """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'title':
                sortkey = 'lower_title'
                products = products.annotate(lower_title=Lower('title'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "You didn't enter any search criteria!")    # noqa
            return redirect(reverse('item_list'))

            queries = Q(title__icontains=query) | Q(description__icontains=query)    # noqa
            products = products.filter(queries)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")    # noqa
                return redirect(reverse('item_list'))

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, "store/item_list.html", context)


def item_view(request, product_id):

    """ A view to see product details and comments"""

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
            form.instance.product = product
            form.instance.user = request.user
            form.save()
            messages.success(request, "Your comment is pending approval!")
            return redirect(item_view, product_id)


@login_required()
def add_product(request):
    """Add product to the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, no access - admins only!")
        return redirect(reverse("item_list"))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(
                request, f"Successfully added a product: {product.title}!")
            return redirect(reverse("item_view", args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to add the product. Please \
                check the form and try again.",
            )
    else:
        form = ProductForm()

    form = ProductForm()
    template = 'store/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """Method to edit an exisiting store product"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, no access - admins only!")
        return redirect(reverse("item_list"))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Successfully updated a product: {product.title}!")
            return redirect(reverse("item_view", args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to update product. Please \
                check the form and try again.",
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.title}")

    template = "store/edit_product.html"
    context = {
        "form": form,
        "product": product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Method to delete an exisiting store product"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, no access - admins only!")
        return redirect(reverse("item_list"))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f"Successfully deleted the product!")
    return redirect(reverse('item_list'))


def handle_404(request, exception):
    return render(request, '404error.html')


def handle_500(request):
    return render(request, '500error.html')
