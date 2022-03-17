from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import CartSerializer, CartBookItemCreateSerializer, OrderDetailSerializer, OrderListSerializer
from .models import Cart, CartBookItem, Order, OrderBookItem, Shipment, Cash, Credit, Transfer
from book.models import BookItem
from user.models import Address

# Create your views here.

class CartDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            cart = Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def put(self, request, pk):
        data = request.data
        try:
            quantity = data['quantity']
            key = data['cartBookItem']
            cart_book_item = CartBookItem.objects.get(pk=key)
            cart_book_item.quantity = quantity
            cart_book_item.save()
            try:
                cart = Cart.objects.get(pk=pk)
            except Cart.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = CartSerializer(cart)
            return Response(serializer.data)
        except:
            return Response(status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk):
        try:
            data = request.data
            quantity = data['quantity']
            check = False
            book_item = BookItem.objects.get(pk=data['bookItem'])
            cart_book_items = CartBookItem.objects.filter(cart_id=pk)
            for cart_book_item in cart_book_items:
                if cart_book_item.bookItem.id == book_item.id:
                    cart_book_item.quantity = cart_book_item.quantity+quantity
                    cart_book_item.save()
                    check = True
            if not check:
                cart = Cart.objects.get(pk=pk)
                CartBookItem(cart = cart, bookItem = book_item, quantity = quantity).save()
            try:
                cart = Cart.objects.get(pk=pk)
            except Cart.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = CartSerializer(cart)
            return Response(serializer.data)
        except:
            return Response(status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            key = request.data['cartBookItem']
            cart_book_item = CartBookItem.objects.get(pk=key)
            cart_book_item.delete()
            try:
                cart = Cart.objects.get(pk=pk)
            except Cart.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = CartSerializer(cart)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class OrderDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        serializer = OrderDetailSerializer(order)
        return Response(serializer.data)

class OrderListAPIView(APIView):
    def get(self, request, pk):
        orders = Order.objects.filter(user_id=pk)
        serializer = OrderListSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        data = request.data
        order = Order.objects.create(user_id=pk)
        order_book_items = data['bookItems']
        for order_book_item in order_book_items:
            book_item = BookItem.objects.get(pk=order_book_item['bookItem'])
            order_book_item_ref = OrderBookItem(bookItem=book_item, quantity=order_book_item['quantity'], order=order)
            order_book_item_ref.save()
        shipment_data = data['shipment']
        address = Address.objects.get(pk=shipment_data['address'])
        shipment_ref = Shipment(order=order, address=address, shippingFee=shipment_data['shippingFee'])
        shipment_ref.save()
        order_book_items = OrderBookItem.objects.filter(order_id=order.id)
        total = 0
        for order_book_item in order_book_items:
            book_item = BookItem.objects.get(pk=order_book_item.bookItem_id)
            total += book_item.price * order_book_item.quantity * (1 - book_item.discount)
        total += shipment_data['shippingFee']
        try:
            cash_data = data['cash']
            cash = Cash(total=total,order=order)
            cash.save()
        except:
            try:
                credit_data = data['credit']
                credit = Credit(total=total, number=credit_data['number'], expDate=credit_data['expDate'],order=order)
                credit.save()
            except:
                try:
                    transfer_data = data['transfer']
                    transfer = Transfer(total=total, number=transfer_data['number'], bankId=transfer_data['bankId'],order=order )
                    transfer.save()
                except:
                    pass
        try:
            order = Order.objects.get(pk=order.id)
        except Order.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        serializer = OrderDetailSerializer(order)
        return Response(serializer.data)