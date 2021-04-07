from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput, CheckboxInput

from .models import Email, UserPermission


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'validate', 'placeholder': 'Username'}))
    email = forms.EmailField(max_length=150, widget=TextInput(attrs={'class': 'validate', 'placeholder': 'Email address'}))
    password1 = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'validate', 'placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Password'}))


class EmailForm(forms.ModelForm):
    email = forms.EmailField(widget=TextInput(attrs={'class': 'validate',
                                                     'placeholder': 'Email address',
                                                     'style': 'width:270px'}))
    permission = forms.BooleanField(label='I have read and accept the Kauta T&Cs and Privacy Policy')

    class Meta:
        model = Email
        fields = ['email', 'permission']


class UserPermissionForm(forms.ModelForm):
    permission = forms.BooleanField()

    class Meta:
        model = UserPermission
        fields = ['permission']
