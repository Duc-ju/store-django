from rest_framework import serializers
from .models import Book, Author, Publisher, Category, BookItem, BookItemImage


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'biography']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    publisher = PublisherSerializer()
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['id', 'title', 'language', 'publicationDate', 'numberOfPages', 'category', 'author', 'publisher']


class BookItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookItemImage
        fields = ['id', 'image', 'index']


class BookItemDetailSerializer(serializers.ModelSerializer):
    images = BookItemImageSerializer(many=True)
    book = BookSerializer()

    class Meta:
        model = BookItem
        fields = ['id', 'price', 'description', 'barcode', 'header', 'discount', 'book', 'images']


class BookItemListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model= BookItem
        fields = ['id','image','header', 'price', 'discount']

    def get_image(self, obj):
        image = BookItemImage.objects.filter(bookItem_id=obj.id, index=0)
        if image.count()==0:
            return ''
        return image[0].image.url