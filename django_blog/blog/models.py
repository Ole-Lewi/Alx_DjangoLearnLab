from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    published_date = models.DateTimeField(auto_now_add=True)
  
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='post')
    created_at = models.DateTimeField(auto_add_now = True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_ (self):
        return(self.title)
    
    def get_absolute_url(self):
        return reverse ('post_detail', kwargs={'pk':self.pk})

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile/pics', blank=True, null= True)