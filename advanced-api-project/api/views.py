from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
from rest_framework import generics, permissions
from .models import Book
from serializers import BookSerializer
from rest_framework.filters import SearchFilter, OrderingFilter


#BookListView: List all books with filtering, ordering and searching capabilities.
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author_name', 'publication_year', 'title'] #allowing filtering by available fields.
    search_fields = ['title', 'author_name'] # allowing filtering by title or author_name.
    order_fields = ['title','publication_year']

#DetailView: List a single book by ID
class BookDetailView(generics.DetailAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

#CreateView: adding a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated] #for authenticated users only

#UpdateView:for modifying an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

#DeleteView: for destroying an unwanted book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
