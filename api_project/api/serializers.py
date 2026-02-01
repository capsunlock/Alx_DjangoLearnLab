# api/serializers.py
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # Include all fields: id, title, and author
        fields = '__all__'