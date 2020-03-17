#ไฟล์นี้ เอาไว้คุมเส้นทงในส่วน ของ folder accounts

from django.urls import path
from . import views #นำเข้าไฟล์ views.py
urlpatterns = [
    path('register/',views.registerPage,name="register"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),

    path('',views.home,name="home"),
    path('user/', views.userPage, name="user-page"),

    path('account/',views.accountsSettings,name="account"),

    path('products/',views.products,name="product"), #call function /views.py function products();
    path('customer/<str:pk_test>/',views.customer,name="customer"), #call function /views.py function customer();

    path('create_order/<str:pk>',views.createOrder,name="create_order"),
    path('update_order/<str:pk>',views.updateOrder,name="update_order"),
    path('delete_order/<str:pk>',views.deleteOrder,name="delete_order"),

]
