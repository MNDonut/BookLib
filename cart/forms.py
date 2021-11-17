from django import forms
from django.forms.widgets import EmailInput, TextInput
from .models import Order
from django.utils.translation import ugettext_lazy as _

class OrderForm(forms.ModelForm):
    userFirstName = forms.CharField(widget=TextInput(attrs={
        'placeholder': 'Ім\'я'
    }))
    userLastName = forms.CharField(widget=TextInput(attrs={
        'placeholder': 'Прізвище'
    }))
    userPatronymic = forms.CharField(widget=TextInput(attrs={
        'placeholder': 'По-батькові'
    }))
    userEmail = forms.CharField(widget=EmailInput(attrs={
        'placeholder': 'Електронна адреса'
    }))
    userPhone = forms.CharField(
        error_messages={'max_length': 'Номер телефону містить забагато символів'},
        widget=TextInput(attrs={
        'placeholder': 'Номер телефону'
    }))

    class Meta:
        model = Order
        fields = ['userFirstName', 'userLastName', 'userPatronymic', 'userEmail', 'userPhone']