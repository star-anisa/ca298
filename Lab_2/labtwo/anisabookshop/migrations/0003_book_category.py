# Generated by Django 4.1.5 on 2023-01-26 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anisabookshop', '0002_rename_books_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.TextField(default='Romance'),
        ),
    ]
