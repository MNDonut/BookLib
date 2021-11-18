from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.deletion import CASCADE
from account.models import CustomUser
from book.models import Book
from django.utils.timezone import now as timenow

def phoneNationalFormatValidator(phone: str):
    if not phone.startswith('+38'):
        raise ValidationError('Введіть номер телефону в міжнародному форматі')
    
def phoneLessNumbersValidator(phone: str):
    if len(phone) < 13:
        raise ValidationError('Номер телефону містить недостатньо символів')

def phoneValidFormatValidator(phone: str):
    if [x.isdigit() for x in phone].count(True) != 12:
        raise ValidationError('Номер телефону містить невірну кількість цифр')

DELIVERY = (
    ('NovaPoshta', 'Нова Пошта'),
    ('UkrPoshta', 'Укрпошта'),
    ('Justin', 'Justin')
)   

class CartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=CASCADE)
    book = models.ForeignKey(Book, on_delete=CASCADE)

    def __str__(self):
        return f"{self.book}"

class Order(models.Model):
    orderNumber = models.AutoField('Номер замовлення', primary_key=True)
    userFirstName = models.CharField('Ім\'я', max_length=32)
    userLastName = models.CharField('Прізвище', max_length=32)
    userPatronymic = models.CharField('По-батькові', max_length=32)
    userEmail = models.EmailField('Електронна адреса', )
    userPhone = models.CharField('Номер телефону', max_length=13, validators=[phoneNationalFormatValidator, phoneLessNumbersValidator, phoneValidFormatValidator])
    delivery = models.CharField('Доставка', choices=DELIVERY, max_length=10, default='NovaPoshta')
    date = models.DateTimeField(default = timenow)
    deliveryAddress = models.CharField(max_length=128, default='')

    def __str__(self):
        return f"Замовлення №{self.orderNumber}"

class OrderedBook(models.Model):
    orderNumber = models.ForeignKey(Order, on_delete=CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=CASCADE)
    book = models.ForeignKey(Book, on_delete=CASCADE)

    def __str__(self):
        return f'{self.orderNumber} - {self.book}'