from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

# 1. Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the DB
    context = {'books': books}  # Pass data to the template
    return render(request, 'relationship_app/list_books.html', context)

# 2. Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'