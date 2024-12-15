from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model().objects.create_user

class UserRegistrationSerializer(serializers.Serializer): #Used for defining serializer fields, particularly for capturing password input securely.
    passwords = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username','bio', 'email', 'profile_picture', 'followers','password']

        def create(self, validated_data):
            user=User.get_user_model().objects.create_user(
                username=validated_data['username'],
                password=validated_data['password'],
                email=validated_data.get('email', '')
            )
            Token.objects.create(user=user) #create a token for the new user
            return user
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.IntegerField(source='followers.count', read_only=True)
    following_count = serializers.IntegerField(source='following.count', read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'followers_count', 'following_count']