from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.shortcuts import reverse
from django.template import loader
from django.contrib import messages

from home.models import Review
from home.forms import RateForm


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def Rate(request):
    user = request.user

    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = user
            rate.save()
            messages.success(
                request,
                "Thank you for your rating and review!",
            )
            return HttpResponseRedirect(reverse('home'))

    else:
        form = RateForm()

    template = 'home/rate.html'

    context = {
        'form': form,
    }

    return render(request, template, context)
