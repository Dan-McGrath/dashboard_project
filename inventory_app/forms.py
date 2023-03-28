from django.forms import ModelForm

from .models import Product, Item, Order, ProductNeeds

class ProductCreateForm(ModelForm):
    class Meta:
        model = Product
        fields = ['items_needed', 'name', 'description', 'sales_cost', 'unit_cost', 'product_count']
        

    
    


class ProductNeedsCreateForm(ModelForm):
    class Meta:
        model = ProductNeeds
        fields = ['items_required']

class ItemCreateForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'distributor', 'unit_cost', 'item_count']
class OrderCreateForm(ModelForm):
    class Meta:
        model = Order
        fields = ['item_id', 'quantity', 'date']



