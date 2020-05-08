# from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models.user import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        Model = User
        field = ['id', 'email', 'password', 'nickname']


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        field = '__all__'
