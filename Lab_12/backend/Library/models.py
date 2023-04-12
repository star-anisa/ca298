from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=40) # charfields have to have a max length
    author = models.CharField(max_length=40)
    genre = models.TextField(default="Romance")
    year = models.IntegerField()
    inventory = models.IntegerField()
    id = models.AutoField(primary_key=True)

    
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)

class Borrow(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    is_returned = models.BooleanField(default=False)
    due_date = models.DateField()
