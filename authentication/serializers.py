from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)

    def validate(self, validated_data):
        if validated_data['username']:
            username = validated_data['username']
            if User.objects.filter(username=username).exists():
                raise serializers.ValidationError('User already exists')
            
        return validated_data

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        user = User.objects.create(username=username, password=password)
        user.set_password(password)
        user.save()

        return {
            "username":validated_data['username'],
            "password":validated_data['password']
        }

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.username
        # ...

        return token