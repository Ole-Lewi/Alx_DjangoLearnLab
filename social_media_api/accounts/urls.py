from django.urls import path
from .views import RegisterView, LoginView, FeedView

urlpatterns = [
    path('register/', RegisterView.as_view(), name ='register'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('/follow/<int:user_id>', FeedView.as_view, name='follow'),
    path('unfollow/<int:user_id>/', name='unfollow')
]