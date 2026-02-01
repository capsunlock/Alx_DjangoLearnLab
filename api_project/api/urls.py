# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Initialize the router
router = DefaultRouter()
# Register the ViewSet
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # 1. Route for the existing BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # 2. Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),
]