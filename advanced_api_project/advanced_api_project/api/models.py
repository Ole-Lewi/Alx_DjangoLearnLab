from django.db import models

# Create your models here.
from django.db import models

# Author model to store author details
class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Author's name

    def __str__(self):
        return self.name  # Return the author's name when referenced


# Book model to store book details
class Book(models.Model):
    title = models.CharField(max_length=200)  # Title of the book
    publication_year = models.IntegerField()  # Year the book was published
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="books"
    )  # One-to-many relationship with Author

    def __str__(self):
        return f"{self.title} by {self.author.name}"  # Return book's title and author's name
