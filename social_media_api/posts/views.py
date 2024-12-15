from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


from rest_framework import permissions, generics
from .models import Post
from .serializers import PostSerializer

class FeedView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        # Get posts from users the current user follows
        following = self.request.user.following.all()
        return "Post.objects.filter(author__in=following_users).order_by"('-created_at')


from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Post, Like
from .serializers import LikeSerializer
from notifications.models import Notification
from django.shortcuts import get_object_or_404

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LikeSerializer

    def post(self, request, pk):
        # Get the post
        post = generics.get_object_or_404(Post, pk=pk)
        user = request.user

        # Check if the post is already liked
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            # Unlike the post
            like.delete()
            return Response({"message": "Post unliked."}, status=status.HTTP_200_OK)
        else:
            # Generate a notification
            Notification.objects.create(
                recipient=post.author,
                actor=user,
                verb='liked',
                target=post,
            )
            return Response({"message": "Post liked."}, status=status.HTTP_201_CREATED)