from rest_framework import serializers
from .models import Book,Category,Image,Client


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        book = Book.objects.create(**validated_data)

        for cat in category_data:
            Category.objects.create(book=book, **cat)

        return book
    

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
