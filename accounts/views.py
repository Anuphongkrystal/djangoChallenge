#เอาไว้สร้างฟังก์ชั่น สำหรับ render ข้อมูล
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm #register and login

from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required  # check สิทธิ์ในการเข้าถึง ไฟล์
from django.contrib.auth.models import Group

from .models import *
from .forms import OrderForm,CreateUserForm,CustomerForm
from .filters import OrderFilter
from .decorators import unauthenticated_user,allowed_users,admin_only

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user=user,
            )

            messages.success(request,'Account was created for ' + username)
            return redirect('login')

    context = {'form':form}
    return render(request,'accounts/register.html',context)

@unauthenticated_user
def  loginPage(request):

    if request.user.is_authenticated:#if session token go back to home page
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request, 'Username or is incorrect')


        context = {}
        return render(request,'accounts/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login') # ต้อง login ก่อน ถึงไปหน้านั้นๆๆได้
#@allowed_users(allowed_roles=['admin'])
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customer = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
            'orders':orders,
            'customers':customers,
            'total_customer':total_customer,
            'total_orders':total_orders,
            'delivered':delivered,
            'pending':pending
    }
    return render(request,'accounts/dashboard.html',context)

@login_required(login_url='login') # ต้อง login ก่อน ถึงไปหน้านั้นๆๆได้
@allowed_users(allowed_roles=['customer']) #user แต่ล่ะ คนต้องอยู่เป็น customer
def userPage(request):
    orders = request.user.customer.order_set.all()


    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    print('ORDERS:', orders)

    context = {
                'orders':orders,
                'total_orders':total_orders,
                'delivered':delivered,
                'pending':pending
    }
    return render(request, 'accounts/user.html',context)

@login_required(login_url='login') # ต้อง login ก่อน ถึงไปหน้านั้นๆๆได้
@allowed_users(allowed_roles=['customer']) #user แต่ล่ะ คนต้องอยู่เป็น customer
def accountsSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST,request.FILES,instance=customer)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request,'accounts/account_settings.html',context)

def products(request):
    products = Product.objects.all()

    return render(request,'accounts/products.html',{'products':products})

@login_required(login_url='login') # ต้อง login ก่อน ถึงไปหน้านั้นๆๆได้
@allowed_users(allowed_roles=['admin'])
def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)

    orders = customer.order_set.all()
    orders_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context =  {
            'customer':customer,
            'orders':orders,
            'orders_count':orders_count,
            'myFilter':myFilter
    }
    return render(request,'accounts/customer.html',context)
@login_required(login_url='login') # ต้อง login ก่อน ถึงไปหน้านั้นๆๆได้
@allowed_users(allowed_roles=['admin'])

def createOrder(request,pk):
    OrderFormSet = inlineformset_factory(Customer,Order,fields=('product','status'), extra=10) ##เพิ่มฟิลด์
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(),instance = customer)
    #form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        #print('Printing POST',request.POST)
        formset = OrderFormSet(request.POST,instance = customer)
        #form = OrderForm(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context =  {'formset':formset}
    return render(request, 'accounts/order_form.html',context)
@login_required(login_url='login') # ต้อง login ก่อน ถึงไปหน้านั้นๆๆได้
@allowed_users(allowed_roles=['admin'])

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
@login_required(login_url='login') # ต้อง login ก่อน ถึงไปหน้านั้นๆๆได้
@allowed_users(allowed_roles=['admin'])

def deleteOrder(request,pk):
    order = Order.objects.get(id=pk) #select ให้ตรงค่าที่ส่งเข้ามา
    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {'item':order}

    return render(request,'accounts/delete.html',context)
