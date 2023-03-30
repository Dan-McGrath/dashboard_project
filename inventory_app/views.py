from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Item, Order, Product, Product_Items
from .forms import ProductCreateForm

# Create your views here.

#Inventory home pagez
class Home(View):

    def get(self, request):
        context = {}
        context['items'] = Item.objects.all()
        context['products'] = Product.objects.all()        
        return render(request, 'inventory_app/inventory_home.html', context)


# Views for Product model



class ProductList(ListView):
    model = Product
    template = 'inventory_app/product_list.html'

    def get(self, request):
        context = {}
        context['product_needs'] = Product_Items.objects.all()
        return render(request, 'inventory_app/product_list.html', context)

class ProductCreate(CreateView):
    model = Product
    template_name = 'inventory_app/product_create_form.html'
    form_class = ProductCreateForm
    success_url = reverse_lazy('product-list')    

class ProductUpdate(UpdateView):
    model = Product
    template_name = 'inventory_app/product_update_form.html'
    fields = ['items', 'name', 'description', 'sales_cost', 'unit_cost']
    success_url = reverse_lazy('product-list')

    #def form_valid(self, form)

    

    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #context['products'] = Product.objects.get(pk=self.kwargs['pk'])
        #return context
    
class ProductDelete(DeleteView):
    model = Product
    template_name = 'inventory_app/delete_form.html'
    success_url = reverse_lazy('product-list')
    

#Views for Item model

class ItemList(ListView):
    model = Item
    template_name = 'inventory_app/item_list.html'

class ItemCreate(CreateView):
    model = Item
    template_name = 'inventory_app/item_create_form.html'
    fields = '__all__'
    success_url = reverse_lazy('item-list')

class ItemUpdate(UpdateView):
    model = Item
    template_name = 'inventory_app/item_update_form.html'
    fields = '__all__'
    success_url = reverse_lazy('item-list')

class ItemDelete(DeleteView):
    model = Item
    template_name = 'inventory_app/delete_form.html'
    success_url = reverse_lazy('item-list')
    
    #success_url = reverse()


#Views for Order model
    

class OrderList(ListView):
    model = Order
    template = 'inventory_app/order_list.html'

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
    template_name = 'inventory_app.delete_form.html'
    fields = ['item_id', 'quantity', 'date']
    #success_url = reverse()


   
    



