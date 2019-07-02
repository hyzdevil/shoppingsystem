from django.urls import path
from apps.userinfo import views

app_name = 'userinfo'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logot/', views.login_out, name='login_out'),
    path('personal/', views.personal, name='personal'),
    path('myaddress/', views.user_address, name='user_address'),
    path('add_address/', views.add_address, name='add_address'),
    path('delete_address/', views.delete_address, name='delete_address'),
    path('getProvince/', views.getProvince, name='getProvince'),
    path('getCity/', views.getCity, name='getCity'),
    path('getDistrict/', views.getDistrict, name='getDistrict')
]