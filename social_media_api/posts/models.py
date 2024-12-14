from django.db import models
from django.contrib.auth import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateField()
    updated_at = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    content = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'