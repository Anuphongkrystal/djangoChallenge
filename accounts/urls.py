#ไฟล์นี้ เอาไว้คุมเส้นทงในส่วน ของ folder accounts

from django.urls import path
from . import views #นำเข้าไฟล์ views.py
urlpatterns = [
    path('',views.home,name="home"),
    path('products/',views.products,name="product"), #call function /views.py function products();
    path('customer/<str:pk_test>/',views.customer,name="customer"), #call function /views.py function customer();
    path('create_order/',views.createOrder,name="create_order"),
]
