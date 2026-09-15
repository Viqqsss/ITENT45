from django.contrib import admin

from .models import CartItem, Product

admin.site.register(Product)
admin.site.register(CartItem)
