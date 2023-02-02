from django.shortcuts import render
from .models import Item, Order

# Create your views here.
def inventory_home(request):
    items = Item.objects.all()
    return render(request, 'inventory_app/inventory.html', {'items': items})

    