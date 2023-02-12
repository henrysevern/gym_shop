from django.shortcuts import render
from .models import *
# from .models import Item


def item_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, "store/item_list.html", context)


def cart(request):
    context = {}
    return render(request, "store/cart.html", context)


def checkout(request):
    context = {}
    return render(request, "store/checkout.html", context)
