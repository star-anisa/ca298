# Generated by Django 4.1.5 on 2023-02-21 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crust',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('thin', 'thin'), ('normal', 'normal'), ('thick', 'thick'), ('gluten free', 'gluten free')], default='normal', max_length=32)),
            ],
        ),
    ]
