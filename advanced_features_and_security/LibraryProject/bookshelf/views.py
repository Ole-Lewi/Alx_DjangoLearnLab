from django.shortcuts import render

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

@permission_required('your_app.can_view', raise_exception=True)
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

@permission_required('your_app.can_create', raise_exception=True)
def post_create(request):
    if request.method == 'POST':
        # Handle creation logic here
        pass
    return render(request, 'post_create.html')

@permission_required('your_app.can_edit', raise_exception=True)
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        # Handle edit logic here
        pass
    return render(request, 'post_edit.html', {'post': post})

@permission_required('your_app.can_delete', raise_exception=True)
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'post_confirm_delete.html', {'post': post})
