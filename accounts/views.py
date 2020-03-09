#เอาไว้สร้างฟังก์ชั่น สำหรับ render ข้อมูล
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customer = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders':orders, 'customers':customers
    ,'total_customer':total_customer,'total_orders':total_orders,'delivered':delivered,
    'pending':pending
    }
    return render(request,'accounts/dashboard.html',context)

def products(request):
    products = Product.objects.all()

    return render(request,'accounts/products.html',{'products':products})

def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)

    orders = customer.order_set.all()
    orders_count = orders.count()
    context =  {'customer':customer,'orders':orders,'orders_count':orders_count}
    return render(request,'accounts/customer.html',context)

def createOrder(request):

    form = OrderForm()
    if request.method == 'POST':
        #print('Printing POST',request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context =  {'form':form}
    return render(request, 'accounts/order_form.html',context)


def updateOrder(request,pk):

    order = Order.objects.get(id=pk) #select ให้ตรงค่าที่ส่งเข้ามา
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/order_form.html',context)


def deleteOrder(request,pk):
    return render(request,'accounts/delete.html')
