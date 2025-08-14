"""
Serializers for the API app.

BookSerializer: Serializes all fields of the Book model and validates that publication_year is not in the future.
AuthorSerializer: Serializes the name and includes a nested list of books using BookSerializer.
The relationship between Author and Book is handled by the 'books' related_name on the Book model's ForeignKey.
"""
from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
