from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/',blank = True, Null = True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')

def _str_(self):
    return self.username