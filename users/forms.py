from django import forms
from django.contrib.auth.models import User
from users.models import Profile

class SignupForm(forms.Form):
    """Signup form"""
    username= forms.CharField(min_length=5,max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(min_length=8,max_length=70, widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control'}))
    password_confirmation = forms.CharField( min_length=8, max_length=70, widget=forms.PasswordInput(attrs={'placeholder': 'Password Confirmation','class': 'form-control'}))