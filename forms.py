from django import forms
from django.forms import ModelForm
from .models import user

class detail_form(forms.Form):
    first_name=forms.CharField(required="True")
    last_name=forms.CharField(required="True")
    address=forms.CharField(required="True")
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    zipcode = forms.IntegerField()
    email = forms.EmailField()
    phone_number = forms.IntegerField()