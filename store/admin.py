from django.contrib import admin

# Register your models here.
from .models import *
from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'price',
        'rating',
        'image',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'approved', 'created_on',)


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Comment)
