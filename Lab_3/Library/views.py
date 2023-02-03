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


