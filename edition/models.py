from django.db import models
from unidecode import unidecode
from django.utils.text import slugify

class Edition(models.Model):
    title = models.CharField(max_length=64)
    slug = models.CharField(max_length=70, blank=True)

    def __str__(self):
        return str(self.title).capitalize()

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(f"{self.title}"))
        super(Edition, self).save(*args, **kwargs)