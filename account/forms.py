from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import CustomUser
from django import forms

class RegistrationForm(UserCreationForm):
    firstname = forms.CharField(widget=TextInput(attrs={
        'placeholder': 'Ім\'я'
    }))
    lastname = forms.CharField(widget=TextInput(attrs={
        'placeholder': 'Прізвище'
    }))
    patronymic = forms.CharField(widget=TextInput(attrs={
        'placeholder': 'По-батькові'
    }))
    email = forms.CharField(widget=TextInput(attrs={
        'placeholder': 'Пошта'
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