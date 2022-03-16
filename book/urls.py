from django.contrib import admin
from django.urls import path, include
from .views import BookListAPIView, BookDetailAPIView,\
    BookItemListAPIView, BookItemDetailAPIView, AuthorListAPIView,\
    CategoryListAPIView, PublisherListAPIView

urlpatterns = [
    path('books/', BookListAPIView.as_view()),
    path('books/<int:pk>/', BookDetailAPIView.as_view()),
    path('book_items/', BookItemListAPIView.as_view()),
    path('book_items/<int:pk>/', BookItemDetailAPIView.as_view()),
    path('authors/', AuthorListAPIView.as_view()),
    path('categories/', CategoryListAPIView.as_view()),
    path('publishers/', PublisherListAPIView.as_view())
]