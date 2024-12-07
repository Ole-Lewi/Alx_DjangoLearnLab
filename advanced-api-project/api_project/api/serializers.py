from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# BookSerializer to serialize all fields of the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"  # Include all fields

    # Custom validation for publication_year
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# AuthorSerializer to serialize the Author model and nested books
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serialization of related books

    class Meta:
        model = Author
        fields = ["name", "books"]  # Serialize name and nested books
