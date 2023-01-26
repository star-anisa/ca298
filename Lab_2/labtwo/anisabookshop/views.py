from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def view_all_books(request):
    all_books = Book.objects.all()
    return render(request, 'all_books.html', {'books':all_books})

def view_single_book(request, bookid):
	single_book = get_object_or_404(Book, id=bookid)
	return render(request, 'single_book.html', {'book':single_book})

def view_books_by_year(request, year):
    # query all bokks for a particular year
    books_by_year = Book.objects.filter(year=year)
    # return them as a list to the front-end
    return render(request,'all_books.html', {'books':books_by_year}  )

def view_books_by_category(request, category):
    # query all books for a particular category
    view_books_by_category = Book.objects.filter(category=category)
    # return them as a list to the front-end
    return render(request,'all_books.html', {'books':view_books_by_category}  )

def view_books_year_categpry(request, year, category):
    books_by_year_category = Book.objects.filter(year=year, price=category) 
    return render(request,'all_books.html', {'books':books_by_year_category}  )