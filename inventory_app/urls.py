from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='inventory-home'),
    path('products/', views.ProductList.as_view(), name ='product-list'),
    path('product/create/', views.ProductCreate.as_view(), name='product-create'),
    path('product/update/<str:pk>', views.ProductUpdate.as_view(), name='product-update'),
    path('product/delete/<str:pk>', views.ProductDelete.as_view(), name='product-delete'),
    path('items/', views.ItemList.as_view(), name='item-list'),
    path('items/create/', views.ItemCreate.as_view(), name='item-create'),
    path('item/update/<str:pk>', views.ItemUpdate.as_view(), name='item-update'),
    path('item/delete/<str:pk>', views.ItemDelete.as_view(), name='item-delete'),
    path('orders/', views.OrderList.as_view(), name='order-list'),
    path('order/update/<str:pk>', views.OrderUpdate.as_view(), name='order-update'),
    path('order/delete/<str:pk>', views.OrderDelete.as_view(), name='order-delete'),
    
]