from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

# Initialize the router
router = DefaultRouter()

# Register the ViewSets
# The first argument is the URL prefix (e.g., 'posts' results in /api/posts/)
# The second argument is the ViewSet itself
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

# The router.urls property contains all the auto-generated URL patterns
urlpatterns = [
    path('', include(router.urls)),
]