from django.contrib import admin
from .models import Item, Product, Order, Product_Items
# Register your models here.
admin.site.register(Product)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Product_Items)