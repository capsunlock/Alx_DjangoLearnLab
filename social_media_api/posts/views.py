from rest_framework import viewsets, permissions, filters, generics, status  # Ensure filters is imported
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

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
        comment = serializer.save(author=self.request.user)
        post = comment.post
        
        # Notify post author if someone else comments
        if post.author != self.request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=self.request.user,
                verb="commented on your post",
                target=post,
                target_content_type=ContentType.objects.get_for_model(Post),
                target_object_id=post.id
            )


class PostFeedView(generics.ListAPIView):
    """
    Returns posts from users that the current user follows.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # 1. Access the users the current user is following
        following_users = self.request.user.following.all()
        
        # 2. Filter posts where the author is in the following_users list
        # We use .order_by('-created_at') to ensure the most recent posts are at the top
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
    
class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Requirement: Check for user authentication (handled by permission_classes)
        # Requirement: Handle liking posts
        post = get_object_or_404(Post, pk=pk)
        
        # Requirement: Prevent users from liking a post multiple times
        # get_or_create returns a tuple (object, created_boolean)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        if not created:
            return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Requirement: Generate appropriate notifications
        # We only notify the author if they aren't liking their own post
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post,
                target_content_type=ContentType.objects.get_for_model(Post),
                target_object_id=post.id
            )

        return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        
        # Look for an existing like
        like = Like.objects.filter(user=request.user, post=post).first()
        
        if not like:
            return Response({"detail": "You haven't liked this post yet."}, status=status.HTTP_400_BAD_REQUEST)
        
        like.delete()
        return Response({"detail": "Post unliked successfully."}, status=status.HTTP_200_OK)