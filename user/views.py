from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer, UserCreateSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser
from rest_framework.generics import CreateAPIView

class UserDetailAPIView(APIView):

    def get(self, request, pk):
        is_staff = request.user.is_staff
        id = request.user.id
        if not is_staff and id!=pk:
            return Response({
                'status': '400',
                'message': 'Not has permission'
            })
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({
                'status': 404,
                'message': 'User not found'
            })
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UserAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    model = User
    serializer_class = UserCreateSerializer