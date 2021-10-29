from django.db import models
from django.db.models.deletion import CASCADE
from author.models import Author
from edition.models import Edition
from unidecode import unidecode
from django.utils.text import slugify

COVERS = (
    ('Softcover', 'М\'яка'),
    ('Hardcover', 'Тверда'),
    ('Supercover', 'Супер'),
)
PAPERTYPES = (
    ('Newspaper', 'Газетний'),
    ('Offset', 'Офсетний')
)

class Category(models.Model):
    image = models.ImageField(upload_to='book_images/category_images')
    title = models.CharField('Назва', max_length=128)
    slug = models.CharField(blank=True, max_length=128)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return str(self.title).capitalize()

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        super(Category, self).save(*args, **kwargs)


class Book(models.Model):
    image = models.ImageField('Зображення', blank=False, upload_to='book_images')
    title = models.CharField('Назва', max_length=128)
    price = models.DecimalField('Ціна', max_digits=6, decimal_places=2)
    author = models.ForeignKey(Author, on_delete=CASCADE, verbose_name='Автор')
    edition = models.ForeignKey(Edition, on_delete=CASCADE, verbose_name='Видавництво')
    category = models.ForeignKey(Category, on_delete=CASCADE, verbose_name='Категорія')
    number = models.PositiveSmallIntegerField('Кількість книг', default=1)
    ISBN = models.PositiveBigIntegerField()
    numberOfPages = models.PositiveIntegerField('Кількість сторінок')
    publicationYear = models.PositiveSmallIntegerField('Рік публікації')
    coverType = models.CharField('Тип обкладинки', max_length=30, choices=COVERS, default='Hardcover')
    paperType = models.CharField('Тип паперу', max_length=30, choices=PAPERTYPES, default='Offset')
    description = models.TextField('Опис')
    isAvailable = models.BooleanField('Доступна', default=True)
    isHot = models.BooleanField('Популярна', default=False)
    isNew = models.BooleanField('Новинка', default=False)
    slug = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return str(self.title).capitalize()

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        super(Book, self).save(*args, **kwargs)