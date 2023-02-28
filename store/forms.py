from .models import Comment, Product
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
