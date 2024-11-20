from django.shortcuts import render
from rest_framework import generics.ListAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework import permissions

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

from rest_framework import viewsets

class BookViewSet(viewsets.ModelViewSet):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer

permission_classes = [permission.IsAuthenticated]  # Only authenticated users can access this view.