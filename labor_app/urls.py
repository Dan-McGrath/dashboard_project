from django.urls import path
from . import views

urlpatterns = [
    path('', views.labor_home, name='labor-home')
]