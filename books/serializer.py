from rest_framework import serializers

from books.models import Book, Author


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    isbn = serializers.CharField(max_length=13)
    genre = serializers.CharField(max_length=8)


class AuthorSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=300)
    last_name = serializers.CharField(max_length=300)


class CreateBooKSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'isbn', 'genre', 'copies', 'author']


class CreateAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email']
