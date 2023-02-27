from django.conf import settings
from django.urls import path

from . import views

urlpatterns = [
    path('', views.payment_view, name="payment"),
    path('payment_start/', views.payment_start, name="payment_start"),
    path('payment_complete/', views.payment_complete, name="payment_complete"),
]
