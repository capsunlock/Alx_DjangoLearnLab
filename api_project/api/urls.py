# api/urls.py
from django.urls import path
from .views import BookList

urlpatterns = [
    # This maps 'books/' to your BookList view
    path('books/', BookList.as_view(), name='book-list'),
]