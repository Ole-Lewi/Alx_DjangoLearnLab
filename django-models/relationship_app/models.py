from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

from django.db.import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    ROLES [
        ('Admin','Admin'),
        ('Librarian', 'Librarian'),
        ('Member','Member')
    ]

    user = models.OneToOneField(Users,on_delete=CASCADE,)
    roles = models.CharField(max_length=10, choices = ROLE_CHOICES)

    def _str_(self):
        return f"{self.user.username}-{self.role}"
    
@receiver (post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver (post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()