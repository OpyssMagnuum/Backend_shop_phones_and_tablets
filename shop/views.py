#!/usr/bin/env python
# -*- coding: utf8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from main.serializers import UserSerializer, ProductSerializer, TagSerializer, BrandSerializer, OrderSerializer, ReviewSerializer, CartSerializer
from shop.models import User, Product, Tag, Brand, Order, Review, Cart
from django.contrib.auth.models import User as UserDjango
from shop.permissions import IsOwnerOrReadOnly

from shop.order_counting import getOrderData, getCart


# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer



class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class MakingOrderViewSet(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def post(self, request):  # По сути нажали на кнопку "Заказать". Удаляем из корзины и -1 каждого товара из корзины
        user_id = int(request.data['user'])  # получаем id юзера на вход
        carts = Cart.objects.all()
        cartsserial = CartSerializer(carts, many=True)
        cart_data = cartsserial.data
        # ПРИМЕР [{'id': 7, 'user': 1, 'product': [2, 3, 4, 1]}]
        our_cart = getCart(user_id=user_id, carts=cart_data)  # Получаем нужную корзину, чтобы сделать всё что нужно
        returning = getOrderData(our_cart)  # то, что нужно положить в БД "orders"
        # Убираем из корзины
        cart_to_del = Cart.objects.get(user=user_id)
        cart_to_del.delete()
        # -1 из количества
        for prod in returning.get('product'):
            product = Product.objects.get(id=prod)
            product.stock_quantity -= 1
            product.save()
        # Добавляем в Orders
        serializer = OrderSerializer(data=returning)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)
