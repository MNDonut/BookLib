# Generated by Django 3.2.8 on 2021-11-17 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20211117_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderNumber',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
