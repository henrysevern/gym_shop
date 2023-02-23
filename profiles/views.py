from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from . import models
from .models import UserProfile


@login_required
def profile(request):
    """
    Display the user's profile page.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)


class profileUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.UserProfile
    fields = ['first_name', 'last_name', 'phone', 'default_address',
              'default_city', 'default_county', 'default_postcode']
    # Function only allows the user to update their own profile

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user

    def form_valid(self, form):
        form.instance.profile = self.request.user
        return super().form_valid(form)
