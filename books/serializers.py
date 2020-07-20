from rest_framework import serializers
from .models import BookInfo, Chapter, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'id',
            'name',
        ]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        author = AuthorSerializer
        fields = [
            'id',
            'name',
            'author',
            'description',
        ]


class ChapterSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Chapter
        fields = [
            'id',
            'title',
            'body',
            'book',
        ]
