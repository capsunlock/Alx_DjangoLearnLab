from django.shortcuts import render
from rest_framework import generics, permissions # Added 'generics' and 'permissions' here
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Book
from .serializers import BookSerializer

"""
Book API Views:
- BookListView: Public read-only access to all books.
- BookDetailView: Public read-only access to a single book.
- BookCreateView: Authenticated users can add new books.
- BookUpdateView: Authenticated users can edit existing books.
- BookDeleteView: Authenticated users can remove books.
"""

# Listview: Retrieve all books. Accessible to everyone (Read-only).
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class_list = [IsAuthenticatedOrReadOnly] #

# DetailView: Retrieve a single book. Accessible to everyone.
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] #

# CreateView: Add a new book. Authenticated users only.
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] #

# UpdateView: Modify an existing book. Authenticated users only.
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] #

# DeleteView: Remove a book. Authenticated users only.
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] #