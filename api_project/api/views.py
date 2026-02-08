from django.shortcuts import render

# api/views.py

from rest_framework import viewsets, permissions
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# This is your existing view from the previous task
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# This is the new ViewSet for full CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Restrict access to authenticated users only
    permission_classes = [permissions.IsAuthenticated]