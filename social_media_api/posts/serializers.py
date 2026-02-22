from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model

class CommentSerializer(serializers.ModelSerializer):
    # Requirement: Handle user relationship correctly
    # We use ReadOnlyField so the author is set automatically in the view
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']

class PostSerializer(serializers.ModelSerializer):
    # Requirement: Handle user relationship correctly
    author = serializers.ReadOnlyField(source='author.username')
    
    # Optional: Nested comments so you can see them when fetching a post
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'comments', 'created_at', 'updated_at']