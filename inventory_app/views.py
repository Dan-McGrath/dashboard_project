from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Item, Order, Product

# Create your views here.

#Inventory home page
def home(request):
    context = {}

    return render(request, 'inventory_app/inventory_home.html', context)


# Views for Product model


class ProductList(ListView):
    model = Product
    template = 'inventory_app.products_list.html'

class ProductCreate(CreateView):
    model = Product
    template_name = 'inventory_app.product_create_form.html'
    fields = ['item_id', 'name', 'description', 'sales_cost', 'product_count']
    #success_url = reverse()

class ProductUpdate(UpdateView):
    model = Product
    template_name = 'inventory_app.product_update_form.html'
    fields = ['item_id', 'name', 'description', 'sales_cost', 'product_count']
    #success_url = reverse()

class ProductDelete(DeleteView):
    model = Product
    template_name = 'inventory_app.product_delete_form.html'
    fields = ['item_id', 'name', 'description', 'sales_cost', 'product_count']
    #success_url = reverse() 

#Views for Item model

class ItemList(ListView):
    model = Item
    template_name = 'inventory_app.item_list.html'

class ItemCreate(CreateView):
    model = Item
    template_name = 'inventory_app.item_create_form.html'
    fields = ['name', 'description', 'distributor', 'unit_cost', 'item_count']
    #success_url = reverse()

class ItemUpdate(UpdateView):
    model = Item
    template_name = 'inventory_app.item_update_form.html'
    fields = ['name', 'description', 'distributor', 'unit_cost', 'item_count']

class ItemDelete(DeleteView):
    model = Item
    template_name = 'inventory_app.item_delete_form.html'
    fields = ['name', 'description', 'distributor', 'unit_cost', 'item_count']
    #success_url = reverse()


#Views for Order model
    

class OrderList(ListView):
    model = Order
    template = 'inventory_app.order_list.html'

class OrderCreate(CreateView):
    model = Order
    template_name = 'inventory_app.order_create_form.html'
    fields = ['item_id', 'quantity', 'date']
    #success_url = reverse()

class OrderUpdate(UpdateView):
    model = Order
    template_name = 'inventory_app.order_update_form.html'
    fields = ['item_id', 'quantity', 'date']
    #success_url = reverse()

class OrderDelete(DeleteView):
    model = Order
    template_name = 'inventory_app.order_delete_form.html'
    fields = ['item_id', 'quantity', 'date']
    #success_url = reverse()


   
    

