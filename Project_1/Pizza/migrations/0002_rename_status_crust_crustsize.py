# Generated by Django 4.1.5 on 2023-02-21 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pizza', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crust',
            old_name='status',
            new_name='crustSize',
        ),
    ]