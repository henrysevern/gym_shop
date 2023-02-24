from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('update/<int:profile_id>', views.edit_profile,
         name="edit_profile")
]
