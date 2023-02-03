from django.shortcuts import render


# Create your views here.
def finance_home(request):
    context = {}

    return render(request, 'financial_app/finance_home.html', context)