from django.urls import path

from . import views

urlpatterns = [
    path('', views.item_list, name="item_list"),
    path('<int:product_id>/', views.item_view, name="item_view"),
    path('product/add_comment/<int:product_id>/', views.add_comment,
         name="add_comment"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path("add/", views.add_product, name="add_product"),
    path("edit/<int:product_id>/", views.edit_product, name="edit_product"),
    path("delete/<int:product_id>/", views.delete_product,
         name="delete_product"),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
]
