from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)


class Publisher(models.Model):
    name = models.CharField(max_length=255)


class Author(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField(max_length=1023)


class Book(models.Model):
    title = models.CharField(max_length=255)
    language = models.CharField(max_length=127)
    publicationDate = models.DateField()
    numberOfPages = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)


class BookItem(models.Model):
    price = models.FloatField(default=0)
    description = models.TextField(max_length=8191)
    barcode = models.CharField(max_length=255)
    header = models.TextField(max_length=1023)
    discount = models.FloatField(default=0)
    book = models.OneToOneField(Book, on_delete=models.CASCADE)


class BookItemImage(models.Model):
    bookItem = models.ForeignKey(BookItem, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/book_item_images/')