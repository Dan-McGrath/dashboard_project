from django.contrib import admin
from .models import Item, Product, Order
# Register your models here.
admin.site.register(Product)
admin.site.register(Item)
admin.site.register(Order)
