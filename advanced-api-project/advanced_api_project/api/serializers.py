from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

#Bookserializer
class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '_all_'   # Serialize all fields of the Book model

def validate_publication_year(self,value):
     current_year = datetime.now().year
     if value > current_year:
        raise serializers.ValidationError("Publication year cannot be in the future.")
     return value

#Authorserializer
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializers(many=True, read_only=True)  # Nested BookSerializer for related books

    class Meta:
        model = Author
        fields = ['name', 'books']  # Include the name and related books