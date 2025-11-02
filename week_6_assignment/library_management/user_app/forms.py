from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'id':'required'}))
    last_name = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'id':'required'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id':'required'}))
    profession = forms.CharField(max_length=100)

    class Meta:
         model = User
         fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class DepositeForm(forms.ModelForm):
    class Meta:
               model = UserProfile
               fields = ['money']

class ProfileUpdateForm(forms.ModelForm):
    password = None

    class Meta :
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']