#0rom djmoney.models.fields import MoneyField
from django.db import models


# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=50, blank=True)
    distributor = models.CharField(max_length=30, blank=True)
    serial_number = models.IntegerField(default=0)
    #item_cost = models.DecimalField(max_digits=6, decmial_places=2)
    #item_cost = models.MoneyField(max_digits=10, decimal_places=2, defualt_currency='USD')

    
    def __str__(self):
        return self.name

    def _str__(self):
        return self.description

    def __str__(self):
        return self.distributor
    
    
    
    
    class Meta:
        ordering = ['name']
        verbose_name = 'item'


