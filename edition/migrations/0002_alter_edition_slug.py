# Generated by Django 3.2.8 on 2021-10-29 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edition', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edition',
            name='slug',
            field=models.CharField(blank=True, max_length=70),
        ),
    ]