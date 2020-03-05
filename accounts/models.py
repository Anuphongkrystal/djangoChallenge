from django.db import models

# Create your models here.
# แยกกัน commit migrate ที่ล่ะ class เพราะมันจะ สร้างไฟล์ให้เราใหม่ทุกครั้งที่ทำการ migrate
class Customer(models.Model):
    name = models.CharField(max_length=200,null = True)
    phone =  models.CharField(max_length=200,null = True)
    email =  models.CharField(max_length=200,null = True)
    date_created = models.DateTimeField(auto_now_add = True,null = True)

    #show name on table custommer
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
            ('Indoor','Indoor'),
            ('Out Door','Out Door'),
    )
    name = models.CharField(max_length=200,null = True)
    price = models.FloatField(null = True)
    category = models.CharField(max_length=200,null = True,choices=CATEGORY)
    deescription = models.CharField(max_length=200,null = True)
    date_created =  models.DateTimeField(auto_now_add = True,null = True)

class Order(models.Model):
    STATUS = (
            ('Pending','Pending'),
            ('Out for delivery','Out for delivery'),
            ('Delivered','Delivered'),
    )
    #customer =
    #product =
    date_created = models.DateTimeField(auto_now_add = True,null = True)
    status = models.CharField(max_length=200,null = True,choices=STATUS)
