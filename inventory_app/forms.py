from django.forms import ModelForm

from .models import Product, Item, Order, ItemStock, ProductStock, ProductNeeds

class ProductCreateForm(ModelForm):
    class Meta:
        model = Product
        fields = ['items_needed', 'name', 'description', 'sales_cost', 'unit_cost']
    
class ProductNeedsCreateForm(ModelForm):
    class Meta:
        model = ProductNeeds
        fields = ['items_required']

class ItemCreateForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'distributor', 'unit_cost']

class OrderCreateForm(ModelForm):
    class Meta:
        model = Order
        fields = ['item_id', 'quantity', 'date']

class ItemStockCreateForm(ModelForm):
    class Meta:
        model = ItemStock
        fields = ['item', 'item_count']

class ProductStockCreateForm(ModelForm):
    class Meta:
        model = ProductStock
        fields = ['product_id', 'current_count']