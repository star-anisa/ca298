
from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Customer
		fields = ['id','name']
	
class BookSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Book
		fields = ['title','genre', 'year', 'author', 'inventory']
    
class BorrowSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Borrow
		fields = ['id','customer','due_date', 'is_returned', 'book']
