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

    def _str__(self):
        return self.description

    def __str__(self):
        return self.distributor

    def add_item(self):
        pass
    
    
    
    class Meta:
        ordering = ['name']
        verbose_name = 'item'


class Order(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total_cost = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

