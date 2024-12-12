from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Tokens

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username','bio', 'email', 'profile_picture', 'followers']
        