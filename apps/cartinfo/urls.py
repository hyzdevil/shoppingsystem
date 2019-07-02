from django.urls import path
from . import views

app_name = 'cartinfo'

urlpatterns = [
    path('add_cart/', views.add_cart, name='add_cart'),
    path('cart/', views.cart_info, name='cart_info'),
    path('delete_goods/<each_goods_id>/', views.delete_goods, name='delete_goods'),
    path('order/', views.order, name='order'),
    path('add_order/', views.add_order, name='add_order'),
    path('place_order/', views.place_order, name='place_order')
]