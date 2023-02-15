
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import JsonResponse # import the jsonresponse object
from rest_framework import viewsets
from .models import *
from .serializers import *


def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def view_all_books(request):
    all_books = Book.objects.all()
    return render(request, 'all_books.html', {'books':all_books})

def view_single_book(request, bookid):
    single_book = get_object_or_404(Book, id=bookid)
    not_returned = Borrow.objects.filter(book=bookid, is_returned = False)
    borrowed_by = Borrow.objects.filter(book=bookid)
    return render(request, 'single_book.html', {'book':single_book, 'not_returned' :not_returned, 'borrowed_by':borrowed_by})

def view_books_by_year(request, year):
    # query all bokks for a particular year
    books_by_year = Book.objects.filter(year=year)
    # return them as a list to the front-end
    return render(request,'all_books.html', {'books':books_by_year}  )

def view_books_by_genre(request, genre):
    # query all books for a particular genre
    view_books_by_genre = Book.objects.filter(genre=genre)
    # return them as a list to the front-end
    return render(request,'all_books.html', {'books':view_books_by_genre}  )

def view_books_year_genre(request, year, genre):
    books_by_year_genre = Book.objects.filter(year=year, genre=genre) 
    return render(request,'all_books.html', {'books':books_by_year_genre}  )

def customer(request, id):
    cust = Customer.objects.get(id=id)
    not_returned = Borrow.objects.filter(customer=id, is_returned = False)
    returned = Borrow.objects.filter(customer = id, is_returned = True)
    return render(request, 'customer.html', {'not_returned':not_returned, 'returned' :returned, 'cust':cust})

def api_add(request):
	num1 = float(request.GET.get('num1',1)) 
	num2 = float(request.GET.get('num2',1))
	added = num1 + num2 # calculate the added value
	resp_dict = {'result':added}
	return JsonResponse(resp_dict) # return the dict as a json respone

def api_subtract(request):
    num1 = float(request.GET.get('num1',1)) 
    num2 = float(request.GET.get('num2',1))
    subtracted = num1 - num2
    resp_dict = {'result':subtracted}
    return JsonResponse(resp_dict)

def api_multiply(request):
    num1 = float(request.GET.get('num1',1)) 
    num2 = float(request.GET.get('num2',1))
    multiplied = num1 * num2
    resp_dict = {'result':multiplied}
    return JsonResponse(resp_dict)

def api_divide(request):
    num1 = float(request.GET.get('num1',1)) 
    num2 = float(request.GET.get('num2',1))
    divided = num1 / num2
    resp_dict = {'result':divided}
    return JsonResponse(resp_dict)

def api_exponential(request):
    num1 = float(request.GET.get('num1',1)) 
    num2 = float(request.GET.get('num2',1))
    exp = num1 ** num2
    resp_dict = {'result':exp}
    return JsonResponse(resp_dict)

## viewset for customers
class CustomerViewSet(viewsets.ModelViewSet):
	serializer_class = CustomerSerializer
	queryset = Customer.objects.all()

class BookViewSet(viewsets.ModelViewSet):
	serializer_class = BookSerializer
	queryset = Book.objects.all()

class BorrowViewSet(viewsets.ModelViewSet):
	serializer_class = BorrowSerializer
	queryset = Borrow.objects.all()

