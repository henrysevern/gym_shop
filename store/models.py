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


class Product(models.Model):
    """
    Items model
    """
    title = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    # Allows the page to load without error if the item contains no image
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    """
    Order model
    """
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,
                                 blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    # Gets the cart total for the cart and checkout page
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    # Gets the item total for the cart and checkout page
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    """
    Order item model
    """
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True,
                                null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True,
                              null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    # Gets the total for to quantity of products in the cart
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    """
    Shipping address model
    """
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,
                                 blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True,
                              null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    county = models.CharField(max_length=200, null=True)
    postcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
