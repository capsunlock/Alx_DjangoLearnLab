from django.shortcuts import render

# api/views.py
# api/views.py
from rest_framework import viewsets
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# This is your existing view from the previous task
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# This is the new ViewSet for full CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing book instances.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer