from rest_framework import serializers

from blog.models.post import Post


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        field = ['title', 'body', 'modify_password']