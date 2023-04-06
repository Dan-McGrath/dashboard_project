from django import forms

from .models import Product, Item, Order, Product_Items

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'sales_cost', 'unit_cost', 'product_count', 'items']
        
    name = forms.CharField()
    description = forms.Textarea()
    items = forms.ModelMultipleChoiceField(
        queryset = Item.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )
    
class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Product_Items
        fields = ['product', 'item', 'item_qty']
    
    items = forms.ModelMultipleChoiceField(
        queryset = Item.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )
    
# class ProductCreateForm(forms.ModelForm):
#     class Meta:
#         model = Product_Items
#         fields = ['']
    
    
    
class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
    

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['item_id', 'quantity', 'date']



