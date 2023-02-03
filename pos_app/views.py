from django.shortcuts import render

# Create your views here.
def pos_home(request):
    context = {}

    return render(request, 'pos_app/pos_home.html', context)