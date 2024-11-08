# relationship_app/urls.py
from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    # URL pattern for the function-based view that lists all books
    path('books/', views.list_books, name='list_books'),

    # URL pattern for the class-based view that shows details of a specific library
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login')
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout')
    path('register/',view.Register(template_name='relationship_app/register.html'), name='register')
]
