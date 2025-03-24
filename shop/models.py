#!/usr/bin/env python
# -*- coding: utf8 -*-
from django.db import models
from django.contrib.auth.models import User as UserDjango


PRODUCT_CHOICES = (
    ('tablet', 'планшет'),
    ('phone', 'телефон'),
)

ORDER_CHOICES = (
    ('issued', 'Оформлен'),
    ('packing', 'Отправлен на сборку'),
    ('packed', 'Собран'),
    ('sorted', 'Отсортирован'),
    ('onTheWay', 'В пути'),
    ('delivered', 'Доставлен'),
    ('obtained', 'Получен'),
    ('cancelled', 'Отменён'),
)

RATING_CHOICES = (
    ('1star', '1'),
    ('2star', '2'),
    ('3star', '3'),
    ('4star', '4'),
    ('5star', '5'),
)


# Create your models here.
class User(models.Model):  # Пользователь с уникальным мейлом и телефоном
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.CharField(max_length=256, unique=True)
    phone = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Brand(models.Model):  # Бренд товара
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Tag(models.Model):  # Возможные теги товара
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)

    def __str__(self):
        return self.name


class Product(models.Model):  # Товар, связь с брендом
    name = models.CharField(max_length=256)
    category = models.CharField(max_length=20, choices=PRODUCT_CHOICES)
    tags = models.ManyToManyField(Tag, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='products')
    price = models.IntegerField()
    stock_quantity = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(UserDjango, on_delete=models.CASCADE, related_name='orders')
    product = models.ManyToManyField(Product, related_name='orders')
    total_price = models.IntegerField()
    status = models.CharField(max_length=64, choices=ORDER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)  # f'{self.user.first_name} {self.user.last_name}'


class Review(models.Model):
    user = models.ForeignKey(UserDjango, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.CharField(max_length=64, choices=RATING_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)


class Cart(models.Model):
    user = models.ForeignKey(UserDjango, on_delete=models.CASCADE, related_name='cart')
    product = models.ManyToManyField(Product, related_name='cart')

    def __str__(self):
        return str(self.user.username)  # f'{self.user.first_name} {self.user.last_name}'







