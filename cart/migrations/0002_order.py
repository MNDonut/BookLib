# Generated by Django 3.2.8 on 2021-11-17 19:23

import cart.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userFirstName', models.CharField(max_length=32)),
                ('userLastName', models.CharField(max_length=32)),
                ('userPatronymic', models.CharField(max_length=32)),
                ('userEmail', models.EmailField(max_length=254)),
                ('userPhone', models.CharField(max_length=13, validators=[])),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]