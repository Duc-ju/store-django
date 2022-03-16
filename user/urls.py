from django.urls import path
from .views import UserDetailAPIView, UserAPIView


urlpatterns = [
    path('<int:pk>/', UserDetailAPIView.as_view()),
    path('', UserAPIView.as_view())
]
