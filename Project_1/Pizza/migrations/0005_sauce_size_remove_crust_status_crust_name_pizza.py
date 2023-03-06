# Generated by Django 4.1.5 on 2023-02-21 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pizza', '0004_alter_crust_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sauce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=1, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=1, max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='crust',
            name='status',
        ),
        migrations.AddField(
            model_name='crust',
            name='name',
            field=models.CharField(default=1, max_length=50),
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crust', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pizza.crust')),
                ('sauce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pizza.sauce')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pizza.size')),
            ],
        ),
    ]