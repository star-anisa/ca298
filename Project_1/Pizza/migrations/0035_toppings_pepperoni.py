# Generated by Django 4.1.5 on 2023-02-26 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pizza', '0034_alter_toppings_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='toppings',
            name='pepperoni',
            field=models.BooleanField(default=True),
        ),
    ]
