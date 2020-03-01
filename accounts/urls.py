#ไฟล์นี้ เอาไว้คุมเส้นทงในส่วน ของ folder accounts

from django.urls import path
from . import views #นำเข้าไฟล์ views.py
urlpatterns = [
    path('',views.home),
    path('products/',views.products), #call function /views.py function products();
    path('customer/',views.customer), #call function /views.py function customer();
]
