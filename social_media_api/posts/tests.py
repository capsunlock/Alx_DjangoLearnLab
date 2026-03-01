from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from .models import Post, Like
from notifications.models import Notification

# Create your tests here.

User = get_user_model()

class SocialFeatureTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_a = User.objects.create_user(username='userA', password='password123')
        self.user_b = User.objects.create_user(username='userB', password='password123')
        self.post = Post.objects.create(author=self.user_b, title="Test Post", content="Content")
        self.client.force_authenticate(user=self.user_a)

    def test_like_post_creates_notification(self):
        """Test that liking a post adds a record and notifies the author."""
        url = f'/api/posts/{self.post.id}/like/'
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Like.objects.count(), 1)
        
        # Verify notification for User B
        notification = Notification.objects.get(recipient=self.user_b)
        self.assertEqual(notification.actor, self.user_a)
        self.assertEqual(notification.verb, "liked your post")

    def test_cannot_like_twice(self):
        """Test the unique_together constraint logic."""
        url = f'/api/posts/{self.post.id}/like/'
        self.client.post(url) # First like
        response = self.client.post(url) # Second like
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Like.objects.count(), 1)