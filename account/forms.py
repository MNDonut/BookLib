from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import CustomUser
from django import forms

class RegistrationForm(UserCreationForm):
    firstname = forms.CharField(widget=TextInput(attrs={
        'placeholder': 'Ім\'я',
        'autofocus': True
    }))
    lastname = forms.CharField(widget=TextInput(attrs={
        'placeholder': 'Прізвище'
    }))
    patronymic = forms.CharField(widget=TextInput(attrs={
        'placeholder': 'По-батькові'
    }))
    email = forms.CharField(widget=TextInput(attrs={
        'placeholder': 'Електронна пошта'
    }))
    password1 = forms.CharField(widget=PasswordInput(attrs={
        'placeholder': 'Пароль'
    }))
    password2 = forms.CharField(widget=PasswordInput(attrs={
        'placeholder': 'Повторіть пароль'
    }))

    class Meta:
        model = CustomUser
        # you should show all fields added in you model
        fields = ['firstname', 'lastname', 'patronymic', 'email', 'password1', 'password2']


# you don't have to override backend because you set USERNAME_FIELD = 'email'
# and it uses 'email' as the 'username' field

# but if you want to add placeholders into fields, you should create
# custom form, where username is you USERNAME_FIELD

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={
        'placeholder': 'Електронна пошта',
        'autofocus': True
    }))
    password = forms.CharField(widget=PasswordInput(attrs={
        'placeholder': 'Пароль'
    }))