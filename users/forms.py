from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import AdoptionModel


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AdoptionModelForm(forms.ModelForm):
    class Meta:
        model = AdoptionModel
        fields = ['name', 'email', 'phone_number', 'address']
