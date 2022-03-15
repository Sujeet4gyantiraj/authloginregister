from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import models
from .models import CustomUser,TwitterKey,Postfile
from django.db.models import fields
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'full_name','password','mobile','email')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'full_name', 'password', 'mobile','email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(full_name=validated_data['full_name'], password = validated_data['password'] ,mobile=validated_data['mobile'], email=validated_data['email'])
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentials Passed.')
    

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postfile
        fields = "__all__"


class TwitterKeySerializer(serializers.ModelSerializer):
    API_KEY=serializers.CharField(max_length=100,required=True)
    API_SECRET=serializers.CharField(max_length=100,required=True)
    ACCESS_TOKEN=serializers.CharField(max_length=100,required=True)
    ACCESS_TOKEN_SECRET=serializers.CharField(max_length=100,required=True)
    

    class Meta:
        model = TwitterKey
        fields = ['API_KEY','API_SECRET','ACCESS_TOKEN','ACCESS_TOKEN_SECRET']
