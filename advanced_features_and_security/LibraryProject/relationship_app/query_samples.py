import os
import sys
import django

# Setup path to find the settings module
# We move up one level to find 'LibraryProject' folder
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)

# Specify the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')

# Initialize Django
django.setup()

# Import models AFTER django.setup()
from relationship_app.models import Author, Book, Library, Librarian

# --- QUERY 1: Query all books by a specific author ---
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        # Using filter() as per common task requirements
        books = Book.objects.filter(author=author)
        print(f"\nBooks written by '{author_name}':")
        for book in books:
            print(f"- {book.title}")
        return books
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")
        return None

# --- QUERY 2: List all books in a library ---
def list_all_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        # Using .all() to retrieve related ManyToMany objects
        books = library.books.all()
        print(f"\nBooks available in '{library_name}':")
        for book in books:
            print(f"- {book.title}")
        return books
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None

# --- QUERY 3: Retrieve the librarian for a library ---
def get_librarian_for_library(library_name):
    try:
        # Get the library instance first
        library = Library.objects.get(name=library_name)
        # Retrieve the librarian associated with this library (One-to-One)
        librarian = Librarian.objects.get(library=library)
        print(f"\nLibrarian for '{library_name}': {librarian.name}")
        return librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        print(f"Librarian or Library '{library_name}' not found.")
        return None

if __name__ == "__main__":
    # Test with the data you added earlier
    print("--- Running Relationship Queries ---")
    get_books_by_author("Lemony Snicket")
    list_all_books_in_library("The Grim Library")
    get_librarian_for_library("The Grim Library")