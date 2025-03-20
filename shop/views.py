#!/usr/bin/env python
# -*- coding: utf8 -*-

from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from main.serializers import UserSerializer, ProductSerializer, TagSerializer, BrandSerializer, OrderSerializer, ReviewSerializer, CartSerializer
from shop.models import User, Product, Tag, Brand, Order, Review, Cart

from shop.order_counting import getOrderData, getCart, addToOrderBD


# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class MakingOrderViewSet(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = CartSerializer

    def post(self, request):  # По сути нажали на кнопку "Заказать". Удаляем из корзины и -1 каждого товара из корзины
        user_id = int(request.data['user'])  # получаем id юзера на вход
        carts = Cart.objects.all()
        cartsserial = CartSerializer(carts, many=True)
        cart_data = cartsserial.data
        our_cart = getCart(user_id=user_id, carts=cart_data)  # Получаем нужную корзину, чтобы сделать всё что нужно
        returning = getOrderData(our_cart)  # то, что нужно положить в БД "orders"
        addToOrderBD(returning)
        return Response(returning)

