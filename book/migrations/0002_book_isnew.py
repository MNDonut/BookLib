# Generated by Django 3.2.8 on 2021-10-29 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='isNew',
            field=models.BooleanField(default=False),
        ),
    ]
