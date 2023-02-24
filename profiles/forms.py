from .models import UserProfile
from django import forms


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'phone', 'default_address',
                  'default_city', 'default_county', 'default_postcode']
