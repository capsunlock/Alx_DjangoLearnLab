from rest_framework import viewsets, permissions, filters  # Ensure filters is imported
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

# Create your views here.

# Custom Permission to ensure only authors can edit/delete
class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS are GET, HEAD, or OPTIONS (anyone can see)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the author of the post/comment
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at') # Order by newest first
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    # Enable search filtering
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# CommentViewSet follows the global pagination naturally
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)