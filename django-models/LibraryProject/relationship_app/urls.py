from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    # FBV URL
    path('books/', list_books, name='list_books'),
    # CBV URL - Note the use of .as_view() and <int:pk>
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]