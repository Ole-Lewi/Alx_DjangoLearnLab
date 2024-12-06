from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView
from django.views import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fiels = ['username','email','password 1','password 2']

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm
        if form.is_valid():
            form.save
            messages.success(request, 'Registration successful!')
            return redirect('login')
        else:
            messages.error(request, "Registration failed, fix the errors below")
    else:
        form = CustomUserCreationForm()
        return render (request, 'authentication/register.html', {'form':form})

@login_required
def profile_view(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST.get('email', user.email)
        user.save()
        messages.success(request, "Profile updated successfully!")
        return render(request, 'authentication/profile.html', {'user':request.user})

@receiver(post_save,sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()