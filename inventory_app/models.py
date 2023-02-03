#from djmoney.models.fields import MoneyField
from django.db import models


# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=50, blank=True)
    distributor = models.CharField(max_length=30, blank=True)
    unit_cost = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    item_count = models.IntegerField(default=0)
    #item_cost = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    #item_cost = models.MoneyField(max_digits=10, decimal_places=2, defualt_currency='USD')

    
    def __str__(self):
        return self.name
 
    def add_item(self):
        pass
    
    class Meta:
        ordering = ['name']
        verbose_name = 'item'


class Product(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=50, blank=True)
    sales_cost = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    product_count = models.IntegerField(default=0)


    def __str__(self):
        return self.name

class Order(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    

    def get_total_cost(self):
        return self.quantity * self.item_id.unit_cost
    
    
