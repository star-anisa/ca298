# Generated by Django 4.1.5 on 2023-02-26 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pizza', '0020_alter_carddetails_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expiration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DecimalField(decimal_places=0, max_digits=3)),
                ('month', models.DecimalField(decimal_places=0, max_digits=3)),
            ],
        ),
        migrations.AlterField(
            model_name='carddetails',
            name='cvv',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='carddetails',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='carddetails',
            name='cardnumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pizza.expiration'),
        ),
    ]
