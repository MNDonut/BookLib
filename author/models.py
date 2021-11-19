from django.db import models
# import these modules for autogenerating slugs
from unidecode import unidecode
from django.utils.text import slugify

class Author(models.Model):
    firstname = models.CharField('Ім\'я', max_length=32)
    lastname = models.CharField('Прізвище', max_length=32)
    slug = models.CharField(max_length=70, blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    # you should override the method because when you fill in
    # the fields, the slug field doesn't know values of these fields
    # (if you want to create a slug automatically)
    # but when you save it, the slug knows values
    # moreover, it's wrong to put the slug below into the Author model
    # because it isn't a django.models field
    def save(self, *args, **kwargs):
        # if you input name or surname in lower case it'll call capitalize()
        self.firstname = str(self.firstname).capitalize()
        self.lastname = str(self.lastname).capitalize()
        self.slug = slugify(unidecode(f"{self.firstname} {self.lastname}"))
        super(Author, self).save(*args, **kwargs)