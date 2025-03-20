from django.contrib import admin
from shop.models import User, Product, Tag, Brand, Order, Review, Cart
# Register your models here.

admin.site.register(Product)
admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Brand)
admin.site.register(Order)
admin.site.register(Review)
admin.site.register(Cart)