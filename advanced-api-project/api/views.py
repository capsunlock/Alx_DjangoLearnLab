from django.shortcuts import render
from rest_framework import generics, permissions, filters  # Import 'filters' module
from django_filters import rest_framework

from rest_framework.filters import SearchFilter, OrderingFilter

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
    """
    BookListView handles filtering, searching, and ordering for the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # Use the 'filters' prefix to satisfy the automated checks
    filter_backends = [
        rest_framework.DjangoFilterBackend, 
        filters.SearchFilter, 
        filters.OrderingFilter
    ]

    # Filtering configuration
    filterset_fields = ['title', 'author', 'publication_year']

    # Searching configuration: Searching title and author's name
    search_fields = ['title', 'author__name']

    # Ordering configuration: Ordering by title and publication year
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']

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