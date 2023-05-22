from django import forms
from home.models import Review, RATE_CHOICES


class RateForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), required=False)    # noqa
    rate = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(),
                             required=True)

    class Meta:
        model = Review
        fields = ('text', 'rate')
