from django.shortcuts import render
from .models import Inventory, Item

# Create your views here.
def inventory(request):
    inven = Inventory.objects.all()
    return render(request, 'inventory.html', {'inven': inven})