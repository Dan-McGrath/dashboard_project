from django.forms import ModelForm

from .models import Product, Item, Order, Product_Items

class ProductCreateForm(ModelForm):
    class Meta:
        model = Product
        fields = ['items', 'name', 'description', 'sales_cost', 'unit_cost', 'product_count']
        
    
    
    
class ItemCreateForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class OrderCreateForm(ModelForm):
    class Meta:
        model = Order
        fields = ['item_id', 'quantity', 'date']



