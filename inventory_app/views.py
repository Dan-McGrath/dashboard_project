from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Item, Order, Product

# Create your views here.

#Views for Item model

class ItemList(ListView):
    model = Item
    template_name = 'inventory_app.inventory.html'

class ItemCreate(CreateView):
    model = Item
    template_name = 'inventory_app.item_create_form.html'
    fields = ['name', 'description', 'distributor', 'unit_cost', 'item_count']

class ItemUpdate(UpdateView):
    model = Item
    template_name = 'inventory_app.item_update_form.html'
    fields = ['name', 'description', 'distributor', 'unit_cost', 'item_count']

class ItemDelete(DeleteView):
    model = Item
    template_name = 'inventory_app.item_delete_form.html'
    fields = ['name', 'description', 'distributor', 'unit_cost', 'item_count']


#Views for Order model
    

class OrderView(ListView):
    model = Order
    template = 'inventory_app.inventory_order.html'

class OrderCreate(CreateView):
    model = Item
    template_name = 'inventory_app.order_create_form.html'
    fields = ['item_id', 'quantity', 'date']

class OrderUpdate(UpdateView):
    model = Item
    template_name = 'inventory_app.order_update_form.html'
    fields = ['item_id', 'quantity', 'date']

class OrderDelete(DeleteView):
    model = Item
    template_name = 'inventory_app.order_delete_form.html'
    fields = ['item_id', 'quantity', 'date']


# Views for Product model   
    

class ProductView(ListView):
    model = Order
    template = 'inventory_app.inventory_home.html'

class ProductCreate(CreateView):
    model = Item
    template_name = 'inventory_app.product_create_form.html'
    fields = ['item_id', 'name', 'description', 'sales_cost', 'product_count']

class ProductUpdate(UpdateView):
    model = Item
    template_name = 'inventory_app.product_update_form.html'
    fields = ['item_id', 'name', 'description', 'sales_cost', 'product_count']

class ProductDelete(DeleteView):
    model = Item
    template_name = 'inventory_app.product_delete_form.html'
    fields = ['item_id', 'name', 'description', 'sales_cost', 'product_count'] 