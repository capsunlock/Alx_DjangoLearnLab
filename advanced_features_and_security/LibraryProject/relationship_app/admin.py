from django.contrib import admin
from .models import Author, Book, Library, Librarian, UserProfile

# Registering models that belong to the relationship_app
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    # The permissions are handled by the Meta class in models.py
    # but they will appear here in the "Permissions" section of the Admin UI

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('name', 'library')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_filter = ('role',)