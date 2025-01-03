# Generated by Django 5.1.3 on 2024-12-18 08:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book_tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasketModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ваше имя')),
                ('email', models.EmailField(max_length=254, verbose_name='ваша электронная почта')),
                ('phone_number', models.IntegerField(verbose_name='ваш номер телефона')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_tags.books')),
            ],
        ),
    ]
