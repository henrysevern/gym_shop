from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages


from store.models import Product

def view_cart(request):
    """ A view to return the cart page """

    return render(request, 'cart/cart.html')
