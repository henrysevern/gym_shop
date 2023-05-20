from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Products model
    """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    sku = models.CharField(max_length=254, null=True, blank=True)
    price = models.FloatField()
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
