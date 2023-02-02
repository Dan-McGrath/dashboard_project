from django.db import models
from inventory_app.models import Item

# Create your models here.


class Sale(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total_cost = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    date = models.DateField(auto_now_add=True)
