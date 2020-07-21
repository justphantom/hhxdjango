from rest_framework import serializers
from .models import Post, Category
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
        ]


class PostListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    author = UserSerializer()

    class Meta:
        model = Post
        fields = [
            'title',
            'created_time',
            'excerpt',
            'body',
            'category',
            'author',
            'views',
        ]
        read_only_fields =[
            "created_time",
        ]



class PostRetrieveSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    author = UserSerializer()

    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'created_time',
            'excerpt',
            'category',
            'author',
            'views',
        ]
