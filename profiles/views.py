from datetime import datetime, timedelta
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from store.models import Order

from . import models
from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    """
    Display the user's profile page.
    """
    four_weeks_ago = timezone.now() - timedelta(days=7*4)

    profile = get_object_or_404(UserProfile, user=request.user)

    # get orders in the last four weeks
    recent_orders = Order.objects.filter(
        date_ordered__gte=four_weeks_ago,
        customer=request.user.customer,
        complete=True
    )

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'recent_orders': recent_orders
    }

    return render(request, template, context)


def edit_profile(request, profile_id):
    """Method to update personal profile"""
    if not request.user.is_authenticated:
        messages.error(request, "Sorry, no access - user only!")
        return redirect(reverse("profile"))

    profile = get_object_or_404(UserProfile, pk=profile_id)
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Successfully updated your profile!")
            return redirect(reverse("profile"), args=[profile.id])
        else:
            messages.error(
                request,
                "Failed to update profile. Please \
                check the form and try again.",
            )
    else:
        form = UserProfileForm(instance=profile)
        # messages.info(request, f"You are editing {user.username}'s profile")

    template = "profiles/edit_profile.html"
    context = {
        "form": form,
        "profile": profile,
    }

    return render(request, template, context)
