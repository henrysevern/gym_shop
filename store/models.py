from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    """
    Customer model
    """
    user = models.OneToOneField(User, null=True, blank=True,
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    """
    Items model
    """
    title = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.title


class Order(models.Model):
    """
    Order model
    """
    customer = model.ForeignKey(Customer, on_delete=models.SET_NULL,
                                blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.id


class OrderItem(model.Model):
    """
    Order item model
    """
    product = model.ForeignKey(Item, on_delete=models.SET_NULL,
                               blank=True, null=True)
    order = model.ForeignKey(Order, on_delete=models.SET_NULL,
                             blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


class ShippingAddress(model.Model):
    """
    Shipping address model
    """
    customer = model.ForeignKey(Customer, on_delete=models.SET_NULL,
                                blank=True, null=True)
    order = model.ForeignKey(Order, on_delete=models.SET_NULL,
                             blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    county = models.CharField(max_length=200, null=True)
    postcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
