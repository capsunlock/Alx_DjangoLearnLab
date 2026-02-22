from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # auto_now_add=True sets the date only when the post is first created
    published_date = models.DateTimeField(auto_now_add=True)
    # The ForeignKey links the post to a User. 
    # on_delete=models.CASCADE means if a user is deleted, their posts are too.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
class Profile(models.Model):
    # This links the Profile to the built-in User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
class Comment(models.Model):
    # Establishing Many-to-One relationship with Post
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    
    # Establishing relationship with User (the author of the comment)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # The text content of the comment
    content = models.TextField()
    
    # Automatically set the time when the comment is first created
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Automatically update the time every time the comment is saved
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

    def get_absolute_url(self):
        # After editing a comment, redirect back to the post detail page
        return reverse('post-detail', kwargs={'pk': self.post.pk})
    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()