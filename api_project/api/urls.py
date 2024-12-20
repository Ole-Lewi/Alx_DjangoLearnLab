from django.urls import path, include
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
]

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Your other URLs
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
