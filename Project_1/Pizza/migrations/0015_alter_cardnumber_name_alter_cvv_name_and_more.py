# Generated by Django 4.1.5 on 2023-02-22 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pizza', '0014_alter_expiration_month_alter_expiration_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardnumber',
            name='name',
            field=models.DecimalField(decimal_places=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='cvv',
            name='name',
            field=models.DecimalField(decimal_places=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='expiration',
            name='month',
            field=models.DecimalField(decimal_places=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='expiration',
            name='year',
            field=models.DecimalField(decimal_places=0, max_digits=3),
        ),
    ]
