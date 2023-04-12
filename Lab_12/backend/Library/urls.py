from django.urls import path, include
from . import views
from .views import *
from rest_framework import routers

# create and define our router 
router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet)
router.register(r'book', BookViewSet)
router.register(r'borrow', BorrowViewSet)

urlpatterns = [
   path('', views.index, name="index"),
   path('contact', views.contact, name='contact'),
   path('books', view_all_books, name='all_books'),
   path('books/<int:bookid>', view_single_book, name='single_book'),
   path('books/year/<int:year>', view_books_by_year, name="books_by_year" ),
   path('books/genre/<str:genre>', view_books_by_genre, name="books_by_genre" ),
   path('books/year/<int:year>/genre/<str:genre>',view_books_year_genre ,name="book_year_genre" ),
   path('customer/<int:id>', customer, name='customer'),
   path('add', views.api_add, name='api_add'),
   path('subtract', views.api_subtract, name='api_subtract'),
   path('multiply', views.api_multiply, name='api_multiply'),
   path('divide', views.api_divide, name='api_divide'),
   path('exponential', views.api_exponential, name='api_exponential'),
   path('api/', include(router.urls)), # add the router to our urls
]