# Generated by Django 4.1.5 on 2023-02-26 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pizza', '0045_alter_customerdetails_cvv_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetails',
            name='expiration_month',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], max_length=2, verbose_name='Expiration Month'),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='expiration_year',
            field=models.CharField(choices=[(2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030), (2031, 2031), (2032, 2032), (2033, 2033), (2034, 2034), (2035, 2035), (2036, 2036), (2037, 2037), (2038, 2038), (2039, 2039), (2040, 2040), (2041, 2041), (2042, 2042)], max_length=4, verbose_name='Expiration Year'),
        ),
    ]
