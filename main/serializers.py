from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from shop.models import User, Product, Tag, Brand, Order, Review, Cart


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'created_at']
        # read_only_fields = ['first_name', 'last_name']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

        def create(self, validated_data):
            user_id = validated_data.pop('user_id')
            product_ids = validated_data.pop('product_ids', [])
            user = get_object_or_404(User, pk=user_id)
            products = Product.objects.filter(pk__in=product_ids)

            order = Order.objects.create(user=user, **validated_data)
            order.product.set(products)

            return order


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Cart
        fields = '__all__'
