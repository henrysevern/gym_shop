from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('update/', views.profileUpdate.as_view(),
         name="profile-update")
]
