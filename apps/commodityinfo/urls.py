from django.urls import path

from apps.commodityinfo import views

app_name = 'commodityinfo'

urlpatterns = [
    path('', views.index, name='index'),
    # path('index/', views.index, name='index'),
    path('<int:each_type_id>/', views.typedetail, name='typedetail'),
    path('<int:each_type_id>/<int:commodity_id>/', views.commoditydetail, name='commoditydetail'),
]