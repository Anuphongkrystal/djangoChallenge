#1 .Returns all customer from customer table
customer = Customer.objects.all()

#2.Returns first customer in table
firstCustomer = Customer.objects.first()

#3.Returns last customer in table
lastCustomer  = Customer.objects.last()

#4.Returns single customer by name
customerByname = Customer.objects.get(name='kookkai')

#5.Returns single customer by ID
customerById = Customer.objects.get(id=4)

#6.Returns all orders related to customer (firstCustomer variable set above)
firstCustomer.order_set.all()

#7.Returns  orders customer name :(Query parent model values)
order = Order.objects.first()
parentName = order.customer.name

#8.Returns product from product table with value of "Out Door" in category attribute
product = Product.objects.filter(category="Out Door")

#9. Order/Sort Objects by id
leastToGreatest = Product.objects.all().order_by('id')
greatestToLeast = Product.objects.all().order_by('-id')

#10. Returns all product with tag of "Sports": (Query Many to Many Fields)
productsFiltered = Product.objects.filter(tags__name="Sports")

#11

#Returns the total count for number of time a "Ball"  was ordered by the first customer
ballOrder = firstCustomer.order_set.filter(product__name="Ball").count()

allOrders = {}
for order in firstCustomer.order_set.all():
    if order.product.name in allOrders:
        allOrders[order.product.name] += 1
    else:
        allOrders[order.product.name] = 1
    #Returns : allOrders:{'Ball':2,'BBQ Grill':1}

#RELATED SET EXAMPLE
class ParentModel(models.Model):
    name = models.CharField(max_length=200,null=True)
class ChildModel(models.Model):
    parent = models.ForeignKey(ParentModel)
    name = models.CharField(max_length=200,null=True)

parent = ParentModel.objects.first()
#Return all child models related to parent
parent.childmodel_set.all()
