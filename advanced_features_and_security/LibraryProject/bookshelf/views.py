from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

@permission_required('your_app.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

@permission_required('your_app.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        # Handle creation logic here
        pass
    return render(request, 'book_create.html')

@permission_required('your_app.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        # Handle edit logic here
        pass
    return render(request, 'book_edit.html', {'book': book})

@permission_required('your_app.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'book': book})

