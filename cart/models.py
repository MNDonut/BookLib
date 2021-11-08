from django.db import models
from django.db.models.deletion import CASCADE
from account.models import CustomUser
from book.models import Book

class CartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=CASCADE)
    book = models.ForeignKey(Book, on_delete=CASCADE)

    def __str__(self):
        return f"{self.book}"
