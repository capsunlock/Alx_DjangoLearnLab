from django.shortcuts import render

# api/views.py
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    # This specifies the data to retrieve
    queryset = Book.objects.all()
    # This specifies how to turn that data into JSON
    serializer_class = BookSerializer