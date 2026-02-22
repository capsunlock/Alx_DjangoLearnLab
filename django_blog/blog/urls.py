from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView
)

urlpatterns = [
    # Blog Post CRUD URLs - Updated to be plural and intuitive
    path('', PostListView.as_view(), name='blog-home'),
    path('posts/', PostListView.as_view(), name='posts'), 
    path('posts/new/', PostCreateView.as_view(), name='post-create'), # Changed from post/new/
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # Changed from post/
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-edit'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]