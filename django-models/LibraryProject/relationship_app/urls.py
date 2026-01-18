from django.urls import path
from .views import list_books, LibraryDetailView, admin_view, librarian_view, member_view
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # FBV URL
    path('books/', list_books, name='list_books'),
    # CBV URL - Note the use of .as_view() and <int:pk>
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication URLs
    # We specify the template_name so Django knows where to look
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin_view/', admin_view, name='admin_view'),
    path('librarian_view/', librarian_view, name='librarian_view'),
    path('member_view/', member_view, name='member_view'),
]