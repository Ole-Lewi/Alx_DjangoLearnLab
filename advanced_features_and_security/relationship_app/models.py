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

    from django.db import models

    class Book(models.Model):
        title= models.CharField(max_length=100)
        author= models.CharField(max_length=100)
        published_date=models.DateField()

        class Meta:
             permissions =[
                 ("can_add_book" = "can add book"),
                 ("can_change_book"='can edit book'),
                 ("can_delete_book"="can delete book"),
                
             ]
def _str_(self):
    return self.title

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

# users/models.py
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, date_of_birth, profile_photo=None, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, date_of_birth=date_of_birth, profile_photo=profile_photo, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, date_of_birth, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, date_of_birth, password=password, **extra_fields)

objects = CustomUserManager()

from django.conf import settings
class SomeModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)