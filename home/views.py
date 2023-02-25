from django.shortcuts import render
from django.conf import settings


def index(request):
    """
    A view to return the index page.
    """
    template = 'home/index.html'

    return render(request, template)
