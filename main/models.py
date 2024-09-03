from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Vendor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    address = models.TextField(null = True)

    def __str__(self):
        return self.user.username


    

class ProductCategory(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.title
    

class Product(models.Model):
    category = models.ForeignKey(ProductCategory,on_delete=models.SET_NULL,null=True,related_name='category_product')
    vendor = models.ForeignKey(Vendor,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=200)
    detail = models.TextField(null=True)
    price = models.FloatField()


    def __str__(self):
        return self.title
    



#Customer Model
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.PositiveBigIntegerField()

    def __str__(self):
        return self.user.username
    



#Order Model
class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    order_time=models.DateTimeField(auto_now_add=True)

    
    

#Order Model
class OrderItems(models.Model):
    order = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='order_items')
    product= models.ForeignKey(Product,on_delete=models.CASCADE)


    def __str__(self):
        return self.product.title