from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='inventory_home'),
    path('products/', views.ProductList.as_view(), name ='productlist'),
    path('product/update/<pk>', views.ProductUpdate.as_view(), name='productupdate'),
    path('product/delete/<pk>', views.ProductDelete.as_view(), name='productdelete'),
    path('items/', views.ItemList.as_view(), name='itemlist'),
    path('item/update/<pk>', views.ItemUpdate.as_view(), name='itemupdate'),
    path('item/delete/<pk>', views.ItemDelete.as_view(), name='itemdelete'),
    path('orders/', views.OrderList.as_view(), name='orderlist'),
    path('order/update/<pk>', views.OrderUpdate.as_view(), name='orderupdate'),
    path('order/delete/<pk>', views.OrderDelete.as_view(), name='orderdelete'),
    
]