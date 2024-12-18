# Generated by Django 5.1.3 on 2024-12-18 13:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Basket', '0003_alter_basketmodel_book'),
        ('book_tags', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basketmodel',
            name='choice_check',
            field=models.CharField(choices=[('✅', '✅'), ('❌', '❌')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='basketmodel',
            name='library',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='book_tags.books'),
        ),
        migrations.AlterField(
            model_name='basketmodel',
            name='book',
            field=models.URLField(null=True, verbose_name='укажите ссылку на книгу'),
        ),
    ]
