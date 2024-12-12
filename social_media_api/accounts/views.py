from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import response
from rest_framework.status import status
from django.contrib.auth import authenticate
from rest_framework.authtoken import Token
from .models import CustomUser
from .serializers import UserSerializer

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        user = CustomUser.objects.create_user(
            username=data['username'],
            password=data['password'],
            email=data.get('email', '')
        )
        token, _=Token.objects.get_or_create(user=user)
        return response({'token':token.key}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _=Token.objects.get_or_create(user=user)
            return response({'token':token.key}, status=status.HTTP_200_OK)
        return response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)