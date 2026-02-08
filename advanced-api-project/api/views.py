from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
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
    Enhanced ListView for Books supporting:
    - Filtering: ?title=...&author=...&publication_year=...
    - Searching: ?search=... (matches title or author name)
    - Ordering: ?ordering=title or ?ordering=-publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    
    # Define backends
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter] #
    
    # Configuration for Filtering (exact matches)
    filterset_fields = ['title', 'author', 'publication_year'] #
    
    # Configuration for Search (partial text matches)
    search_fields = ['title', 'author__name'] #
    
    # Configuration for Ordering
    ordering_fields = ['title', 'publication_year'] #
    ordering = ['title']  # Default ordering

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