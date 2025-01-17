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
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    path('register/',auth_views.RegisterView.as_view(template_name='relationship_app/register.html'), name='register'),
]


from django.urls import path
from . import views

urlpatterns= [
    path('admin/', views.admin_view, name='admin_view'),
    path('member/', views.member_view, name='member_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('register/',"views.register"(template_name='relationship_app/register.html'), name='register')
]


    
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_book, name="add_book/"),
    path('edit/<int:pk>/', views.edit_book, name="edit_book/"),
    path('delete/<int:pk>/', views.delete_book, name="delete_book/"),
]


from django.urls import path
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]
