from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import CreateView
from django.urls import reverse_lazy

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_ulr = reverse_lazy('login')
    template_name = 'registration/signup.html'
