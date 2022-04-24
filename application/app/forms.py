from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *


class AuthForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class ExtendedRegisterForm(UserCreationForm):
    username = forms.CharField(min_length=6, label='Логин')
    email = forms.EmailField(label='Адрес электронной почты')
    class Meta:
        model = ExtendedUser
        fields = ('username', 'email', 'password1', 'password2')
