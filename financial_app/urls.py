from django.urls import path
from . import views

urlpatterns = [
    path('', views.finance_home, name='finance_home'),

]