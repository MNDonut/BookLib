from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import CustomUser
from django import forms
from django.core.exceptions import ValidationError

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

    # clean_attribute methods either raise error or return this attribute

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError('Ця електронна адреса зайнята')
        return email

    def clean_password2(self):
        password = self.cleaned_data['password1']
        passwordConfirm = self.cleaned_data['password2']
        if password != passwordConfirm:
            raise ValidationError('Паролі не співпадають')
        if len(passwordConfirm) < 8:
            raise ValidationError('Пароль повинен містити мінімум 8 символів')
        
        return passwordConfirm

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