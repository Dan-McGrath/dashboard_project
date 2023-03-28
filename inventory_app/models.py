#from djmoney.models.fields import MoneyField
from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.


#Item Model

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
    
    def get_absolute_url(self):
        return reverse("item-detail", kwargs={"pk": self.pk})
    

    
    class Meta:
        ordering = ['name']
        verbose_name = 'items'





# Product Model

class Product(models.Model):
    items_needed = models.ManyToManyField(Item, through = 'ProductNeeds')
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=50, blank=True)
    sales_cost = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    unit_cost = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    product_count = models.IntegerField(default=0)     

    def __str__(self):
        return self.name


    class Meta:
        ordering = ['name']
        verbose_name = 'products'

# Many-to-Many Products-Items
class ProductNeeds(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    items_required = models.IntegerField(default=0)

            
    def __str__(self):
        return self.product
    



#Order Model        

class Order(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date = models.DateField(default=timezone.now)
    

    def get_total_cost(self):
        return self.quantity * self.item_id.unit_cost
    
    
