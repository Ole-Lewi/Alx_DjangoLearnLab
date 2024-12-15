from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False, related_name = 'followers', blank=True)
    bio = models.TextField(blank=True,)
    profile_picture = models.ImageField(upload_to='profile_pictures/',blank = True,)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')

def _str_(self):
    return self.username