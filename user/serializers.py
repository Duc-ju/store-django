from rest_framework import serializers
from .models import User, Address
from order.models import Cart

class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model= Address
        fields = ['id', 'fullName', 'phoneNumber', 'city', 'district', 'detail']

class UserSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True)



    class Meta:
        model = User
        fields = ['id', 'username', 'displayName', 'email', 'photoUrl', 'addresses']


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            displayName=validated_data['displayName'],
            email=validated_data['email']
        )
        Cart.objects.create(user_id=user.id)
        return user
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'displayName']