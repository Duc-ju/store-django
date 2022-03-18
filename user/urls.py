from django.urls import path
from .views import UserDetailAPIView, UserAPIView


urlpatterns = [
    path('users/<int:pk>/', UserDetailAPIView.as_view()),
    path('users/', UserAPIView.as_view())
]
