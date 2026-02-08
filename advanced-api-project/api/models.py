from django.db import models

# Create your models here.
class Author(models.Model):
    """Stores author details."""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """Stores book details linked to an Author."""
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    # related_name allows AuthorSerializer to access books easily
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title