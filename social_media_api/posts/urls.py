from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, PostFeedView, LikePostView, UnlikePostView

# Initialize the router
router = DefaultRouter()

# Register the ViewSets
# The first argument is the URL prefix (e.g., 'posts' results in /api/posts/)
# The second argument is the ViewSet itself
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

# The router.urls property contains all the auto-generated URL patterns
urlpatterns = [
    # New Feed Route
    path('feed/', PostFeedView.as_view(), name='post_feed'),
    path('', include(router.urls)),

    path('<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
]