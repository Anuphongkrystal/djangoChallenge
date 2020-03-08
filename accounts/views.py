#เอาไว้สร้างฟังก์ชั่น สำหรับ render ข้อมูล
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    return render(request,'accounts/dashboard.html')

def products(request):
    products = Product.objects.all()

    return render(request,'accounts/products.html',{'products':products})

def customer(request):
    return render(request,'accounts/customer.html')
