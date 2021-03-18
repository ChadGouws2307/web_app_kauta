from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput

from .models import Email


class SignUpForm(UserCreationForm):
    #first_name = forms.CharField(max_length=100, help_text='Last Name')
    #last_name = forms.CharField(max_length=100, help_text='Last Name')
    #email = forms.EmailField(max_length=150, help_text='Valid email address')
    username = forms.CharField(widget=TextInput(attrs={'class': 'validate', 'placeholder': 'Username'}))
    email = forms.EmailField(max_length=150, widget=TextInput(attrs={'class': 'validate', 'placeholder': 'Email address'}))
    password1 = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)   # 'first_name', 'last_name',


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'validate', 'placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Password'}))


class EmailForm(forms.ModelForm):
    email = forms.EmailField(widget=TextInput(attrs={'class': 'validate', 'placeholder': 'Email address'}))

    class Meta:
        model = Email
        fields = ['email']
