from rest_framework import serializers
from .models import Post,Comment,Like

class PostSerializers(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id','author','title', 'content', 'created_at', 'updated_at']

class CommentSerializers(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post_title = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Comment
        fields = ['id','author', 'content', 'created_at', 'updated_at','post', 'post.title']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'created_at']