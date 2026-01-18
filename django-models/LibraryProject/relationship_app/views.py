from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Log the user in after registration
            return redirect('list_books') # Redirect to a page of your choice
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})