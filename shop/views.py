#!/usr/bin/env python
# -*- coding: utf8 -*-

from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from main.serializers import UserSerializer, ProductSerializer, TagSerializer, BrandSerializer, OrderSerializer, ReviewSerializer, CartSerializer
from shop.models import User, Product, Tag, Brand, Order, Review, Cart

from shop.order_counting import getOrderData, getCart


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


class MakingOrderViewSet(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = CartSerializer

    # def post(self, request):  # По сути нажали на кнопку "Заказать". Удаляем из корзины и -1 каждого товара из корзины
    #     user_id = int(request.data['user'])  # получаем id юзера на вход
    #     carts = Cart.objects.all()
    #     cartsserial = CartSerializer(carts, many=True)
    #     cart_data = cartsserial.data
    #     our_cart = getCart(user_id=user_id, carts=cart_data)  # Получаем нужную корзину, чтобы сделать всё что нужно
    #     returning = getOrderData(our_cart)  # то, что нужно положить в БД "orders"
    #     user = User.objects.get(id=user_id)
    #     # Убираем из корзины
    #     cart_to_del = Cart.objects.get(user=user)
    #     cart_to_del.delete()
    #     # -1 из количества
    #     for prod in returning.get('product'):
    #         product = Product.objects.get(id=prod)
    #         product.stock_quantity -= 1
    #         product.save()
    #     # Добавляем в Orders
    #     serializer = OrderSerializer(data=returning)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=400)

