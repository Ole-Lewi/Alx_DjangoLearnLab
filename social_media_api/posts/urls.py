from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/accounts/', include('accounts.urls')),
    path('api/posts/', include('posts.url')),
    path('feed/', FeedView.as_view(), name='feed'),
]
