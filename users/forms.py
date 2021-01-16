from django import forms
from django.contrib.auth.models import User
from users.models import Profile

class SignupForm(forms.Form):
    """Signup form"""
    username= forms.CharField(min_length=5,max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))