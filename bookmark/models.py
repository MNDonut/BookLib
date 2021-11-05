from django.db import models
from django.db.models.deletion import CASCADE
from book.models import Book
from account.models import CustomUser

class BookMark(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=CASCADE)
    book = models.ForeignKey(Book, on_delete=CASCADE)

    def __str__(self):
        return f"{self.book}"
