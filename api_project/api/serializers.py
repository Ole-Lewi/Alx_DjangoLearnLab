from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    Model =Book
    fields = ["title", "author", "published_date"]
    