from django.db import models


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=40)
    title = models.CharField(max_length=40) # charfields have to have a max length
    year = models.IntegerField()
    synopsis = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2) # number from 0.0-999.99
    category = models.TextField(default="Romance")
