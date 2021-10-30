from django import forms

# Create your tests here.
from home_page.models import SubscribeUser


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = SubscribeUser
        fields = '__all__'
