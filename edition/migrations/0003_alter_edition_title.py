# Generated by Django 3.2.8 on 2021-10-29 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edition', '0002_alter_edition_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edition',
            name='title',
            field=models.CharField(max_length=64, verbose_name='Назва'),
        ),
    ]