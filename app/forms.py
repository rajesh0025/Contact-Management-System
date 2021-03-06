from django import forms
from django.contrib.auth.models import User
from . import models


class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

class ContactForm(forms.ModelForm):
    class Meta:
        model=models.Contact
        fields=['name','number','email']