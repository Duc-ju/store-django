from django.urls import path
from .views import CartDetailAPIView, OrderDetailAPIView, OrderListAPIView, CartListAPIView, CartBookItemListAPIView, CartBookItemDetailAPIView


urlpatterns = [
    path('users/<int:pk>/carts/', CartListAPIView.as_view()),
    path('carts/<int:pk>/', CartDetailAPIView.as_view()),
    path('carts/<int:pk>/cart_book_items/', CartBookItemListAPIView.as_view()),
    path('carts/<int:cart_pk>/cart_book_items/<int:cart_book_item_pk>/', CartBookItemDetailAPIView.as_view()),
    path('users/<int:pk>/orders/', OrderListAPIView.as_view()),
    path('orders/<int:pk>/', OrderDetailAPIView.as_view())
]