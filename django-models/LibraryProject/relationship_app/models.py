from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    # ForeignKey: One author can have many books
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=200)
    # ManyToManyField: Many books can be in many libraries
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    # OneToOneField: One library has exactly one librarian
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name