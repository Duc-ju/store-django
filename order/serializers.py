from rest_framework import serializers
from .models import Cart, CartBookItem, Order, OrderBookItem, Shipment, Credit, Cash, Transfer
from book.models import BookItem
from user.serializers import AddressSerializer
from book.serializers import BookItemListSerializer


class CartBookItemSerializer(serializers.ModelSerializer):
    bookItem = BookItemListSerializer(read_only=True)

    class Meta:
        model = CartBookItem
        fields=['id', 'bookItem','quantity']
class CartBookItemCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartBookItem
        fields=['id', 'cart', 'bookItem','quantity']

class CartSerializer(serializers.ModelSerializer):
    bookItems = CartBookItemSerializer(many=True, read_only=True)
    subTotal= serializers.SerializerMethodField(read_only=True)
    numberOfItems = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model= Cart
        fields=['id', 'bookItems', 'subTotal', 'numberOfItems']

    def get_subTotal(self, obj):
        cart_book_items = CartBookItem.objects.filter(cart_id=obj.id)
        sub_total = 0
        for cart_book_item in cart_book_items:
            book_item = BookItem.objects.get(pk=cart_book_item.bookItem_id)
            sub_total += book_item.price*cart_book_item.quantity * (1-book_item.discount)
        return sub_total

    def get_numberOfItems(self, obj):
        cart_book_items = CartBookItem.objects.filter(cart_id=obj.id)
        number_of_items = 0
        for cart_book_item in cart_book_items:
            number_of_items+=cart_book_item.quantity
        return number_of_items

class OrderBookItemSerializer(serializers.ModelSerializer):
    bookItem = BookItemListSerializer(read_only=True)

    class Meta:
        model = OrderBookItem
        fields=['id', 'bookItem','quantity']


class ShipmentSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Shipment
        fields = ['id', 'address', 'shippingFee']

class CashSerializer(serializers.ModelSerializer):

    class Meta:
        model=Cash
        fields=['id', 'total', 'createdAt', 'updatedAt']


class CreditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Credit
        fields = ['id', 'total', 'number', 'expDate', 'createdAt', 'updatedAt']


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ['id', 'total', 'number', 'bankId', 'createdAt', 'updatedAt']

class OrderDetailSerializer(serializers.ModelSerializer):
    bookItems = OrderBookItemSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField(read_only=True)
    shipment = ShipmentSerializer()
    cash = CashSerializer()
    transfer = TransferSerializer()
    credit = CreditSerializer()
    numberOfItem = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'bookItems', 'total', 'numberOfItem','shipment', 'cash', 'transfer', 'credit', 'createdAt', 'updatedAt']


    def get_total(self, obj):
        order_book_items = OrderBookItem.objects.filter(order_id=obj.id)
        total = 0
        for order_book_item in order_book_items:
            book_item = BookItem.objects.get(pk=order_book_item.bookItem_id)
            total += book_item.price * order_book_item.quantity * (1-book_item.discount)
        shipment = Shipment.objects.filter(order_id=obj.id)[0]
        total += shipment.shippingFee
        return total

    def get_numberOfItem(self, obj):
        order_book_items = OrderBookItem.objects.filter(order_id=obj.id)
        number = 0
        for order_book_item in order_book_items:
            number+=order_book_item.quantity
        return number

class OrderListSerializer(serializers.ModelSerializer):
    firstItem = serializers.SerializerMethodField(read_only=True)
    numberOfItem = serializers.SerializerMethodField(read_only=True)
    total = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'firstItem', 'numberOfItem' ,'total']

    def get_firstItem(self, obj):
        order_book_items = OrderBookItem.objects.filter(order_id=obj.id)[0]
        serializer = OrderBookItemSerializer(order_book_items)
        return serializer.data

    def get_numberOfItem(self, obj):
        order_book_items = OrderBookItem.objects.filter(order_id=obj.id)
        number = 0
        for order_book_item in order_book_items:
            number+=order_book_item.quantity
        return number

    def get_total(self, obj):
        order_book_items = OrderBookItem.objects.filter(order_id=obj.id)
        total = 0
        for order_book_item in order_book_items:
            book_item = BookItem.objects.get(pk=order_book_item.bookItem_id)
            total += book_item.price * order_book_item.quantity * (1 - book_item.discount)
        shipment = Shipment.objects.filter(order_id=obj.id)[0]
        total += shipment.shippingFee
        return total
