from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ExtendedRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Имя')
    second_name = forms.CharField(max_length=30, required=False, help_text='Фамилия')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'second_name', 'email', 'password1', 'password2')