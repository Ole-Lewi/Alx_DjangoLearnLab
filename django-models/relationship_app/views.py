from django.shortcuts import render
from .models import Book

def list_books(request):
   
    return(render,"relationship_app/list_books.html", "Book.objects.all()")

from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
 ["relationship_app/library_detail.html"]
