from django.db import models
from django.db.models.fields import CharField, EmailField

# Create your models here.

class Category(models.Model):
    name= models.CharField(blank=False, null=False,max_length=50)
    parent_id=models.ForeignKey('Category', null=False, blank=False,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(autonow=True)

class Admin (models.Model):
    name=models.CharField(max_length=300, null=False, blank=False)
    email=models.EmailField(max_length=300, null=False, blank=False)
    password=models.CharField(max_length=300, null=False, blank=True)
    phone_number=models.IntegerField(null=False, blank=False)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(autonow=True)


class Customer(models.Model):
    name=models.CharField(max_length=300, null=False, blank=False)
    email=models.EmailField(max_length=300, null=False, blank=False)
    password=models.CharField(max_length=300, null=False, blank=True)
    phone_number=models.IntegerField(null=False, blank=False)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(autonow=True)

class Seller(models.Model):
    name=models.CharField(max_length=300, null=False, blank=False)
    email=models.EmailField(max_length=300, null=False, blank=False)
    logo=models.CharField(max_length=300, null=False, blank=False)
    phone_number=models.IntegerField(null=False, blank=False)
    business_number=models.IntegerField(null=False, blank=False)
    status=models.CharField(max_length=300, null=False, blank=False)
    external_url=models.CharField(max_length=300, null=False, blank=False)
    password=models.CharField(max_length=300, null=False, blank=False)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(autonow=True)


class CustomerAddress(models.Model):
    customer_id=models.ForeignKey('Customer', on_delete=models.CASCADE, null=False, blank=False)
    address= models.CharField(max_length=500, null=False, blank=False)
    pin= models.CharField(max_length=200, null=False, blank=False)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(autonow=True)

class Product(models.Model):
    name=models.CharField(max_length=50, null=False, blank=False)
    category_id= models.ForeignKey('Category', on_delete=models.CASCADE,blank=False, null=False )
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(autonow=True)


class Order(models.Model):
    order_number= models.CharField(max_length=100,null=False, blank=False)
    shipping_cost= models.IntegerField(null=False, blank=False)
    status= models.CharField(max_length=300, null=False, blank=False)
    total= models.IntegerField(null=False, blank=False)
    customer_id= models.ForeignKey('Customer', on_delete= models.CASCADE, null=False, blank=False)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(autonow=True)


class OrderProduct(models.Model):
    order_id=models.ForeignKey('Order', on_delete=models.CASCADE, blank=False, null=False)    
    product_id=models.ForeignKey('Product', on_delete=models.CASCADE, null=False, blank=False)
    quantity=models.IntegerField(null=False, blank=False)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(autonow=True)


class Feedback(models.Model):
    message=models.TextField(null=False, blank=True)
    name=models.CharField(max_length=300, null=True, blank=True)
    email=models.EmailField(max_length=300, null=True, blank=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(autonow=True)


class Reviews(models.Model):
    rating= models.IntegerField(null=False, blank=False)
    review=models.TextField(null=True, blank=True)
    customer_id=models.ForeignKey('Customer',on_delete=models.CASCADE, null=False, blank=False)
    product_id=models.ForeignKey('Product', on_delete=models.CASCADE, null=False, blank=False)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(autonow=True)


class Payment(models.Model):
    order_id=models.ForeignKey('Order',on_delete=models.CASCADE, null=False, blank=False)
    amount=models.IntegerField(null=False, blank=True)
    mode=models.CharField(null=False, blank=False, max_length= 300)
    description= models.CharField(null=True, blank=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(autonow=True)


class Delivery(models.Model):
    order_id=models.ForeignKey('Order',on_delete=models.CASCADE, null=False, blank=False)
    customer_address_id=models.ForeignKey('CustomerAddress', on_delete=models.CASCADE, blank=False, null=False )
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(autonow=True)


class Wishlist(models.Model):
    customer_id=models.ForeignKey('Customer',on_delete=models.CASCADE, null=False, blank=False)
    product_id= models.ForeignKey('Product',on_delete=models.CASCADE, null=False, blank=False)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(autonow=True)


class Offer(models.Model):
    product_id= models.ForeignKey('Product',on_delete=models.CASCADE, null=False, blank=False)
    offer_amount= models.IntegerField(null=False, blank=False)
    start_date= models.DateTimeField(null=False, blank=False)
    end_date= models.DateTimeField(null=False, blank=False)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(autonow=True)


class Voucher (models.Model):
    product_id= models.ForeignKey('Product',on_delete=models.CASCADE, null=False, blank=False)
    voucher_amount= models.IntegerField(null=False, blank=False)
    voucher_tag= models.CharField(null=False, blank=False, max_length= 50)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(autonow=True)
