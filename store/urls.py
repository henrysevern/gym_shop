from django.urls import path

from . import views

urlpatterns = [
    path('', views.item_list, name="item_list"),
    path('item_view/', views.item_view, name="item_view"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
]
