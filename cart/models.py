from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.deletion import CASCADE
from account.models import CustomUser
from book.models import Book

# def phoneValidator(phone: str):
#     if '+38' not in phone or [x.isdigit() for x in phone].count(True) != 12:
#         raise ValidationError('Номер телефону введений у невірному форматі!')
        

class CartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=CASCADE)
    book = models.ForeignKey(Book, on_delete=CASCADE)

    def __str__(self):
        return f"{self.book}"

# class Order(models.Model):
#     userFirstName = models.CharField(max_length=32, required=True)
#     userLastName = models.CharField(max_length=32, required=True)
#     userPatronymic = models.CharField(max_length=32, required=True)
#     userEmail = models.EmailField(required=False)
#     userPhone = models.CharField(max_length=13, validators=[phoneValidator])

