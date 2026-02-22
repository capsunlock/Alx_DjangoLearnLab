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
    # Blog Post CRUD URLs
    path('', PostListView.as_view(), name='blog-home'),
    path('post/', PostListView.as_view(), name='post'), 
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    
    # Requirement: URLs containing "post/<int:pk>/delete/" and "post/<int:pk>/update/"
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]