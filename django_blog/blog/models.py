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
    # Linking the comment to a specific post. 
    # related_name='comments' allows us to access comments from a post object (e.g., post.comments.all())
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    
    # Linking to the user who wrote it
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    content = models.TextField()
    
    # Timestamps
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()