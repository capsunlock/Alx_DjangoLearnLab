from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Comment, Post

# Make sure this name is spelled exactly like this:
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # We only want the user to type the content.
        # The 'post' and 'author' will be handled automatically by our views.
        fields = ['content']
        
        # Adding some styling and a placeholder using widgets
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your comment here...',
                'rows': 4,
            }),
        }

    def clean_content(self):
        """
        Custom validation to ensure comments aren't just whitespace or too short.
        """
        content = self.cleaned_data.get('content')
        if not content or len(content.strip()) < 2:
            raise forms.ValidationError("Your comment is a bit too short!")
        return content

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # We only include title and content - The author and published_date are handled automatically.
        fields = ['title', 'content']
        
        # Optional: Add widgets for better styling with your CSS
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter post title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Share your thoughts...'}),
        }