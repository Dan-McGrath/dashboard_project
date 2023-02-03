from django.shortcuts import render

# Create your views here.
def labor_home(request):
    context = {}

    return render(request, 'labor_app/labor_home.html', context)