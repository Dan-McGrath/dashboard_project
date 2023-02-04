from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'name': 'Dan'}
    return render(request, 'my_site/home.html', context)