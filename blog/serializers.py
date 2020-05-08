from blog.models import Board, User, Post, GuestBook
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class GuestbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestBook
        fields = '__all__'
