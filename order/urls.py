from django.urls import path
from .views import CartDetailAPIView, OrderDetailAPIView, OrderListAPIView


urlpatterns = [
    path('carts/<int:pk>/', CartDetailAPIView.as_view()),
    path('orders/user/<int:pk>/', OrderListAPIView.as_view()),
    path('orders/<int:pk>/', OrderDetailAPIView.as_view())
]