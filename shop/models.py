from django.db import models
from django.db.models import constraints
from django.db.models.fields import CharField, EmailField

# Create your models here.

class Category(models.Model):
    name= models.CharField(blank=False, null=False,max_length=50)
    parent_id=models.ForeignKey('Category', null=True, blank=True,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name=models.CharField(max_length=300, null=False, blank=False)
    email=models.EmailField(max_length=300, null=False, blank=False)
    password=models.CharField(max_length=300, null=False, blank=True)
    phone_number=models.IntegerField(null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Seller(models.Model):
    name=models.CharField(max_length=300, null=False, blank=False)
    email=models.EmailField(max_length=300, null=False, blank=False)
    logo=models.CharField(max_length=300, null=True, blank=True)
    phone_number=models.IntegerField(null=True, blank=True)
    business_number=models.IntegerField(null=True, blank=True)
    status=models.CharField(max_length=300, null=False, blank=False, default= 'Unverified')
    external_url=models.CharField(max_length=300, null=True, blank=True)
    password=models.CharField(max_length=300, null=False, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CustomerAddress(models.Model):
    customer_id=models.ForeignKey('Customer', on_delete=models.CASCADE, null=False, blank=False)
    address= models.CharField(max_length=500, null=False, blank=False)
    pin= models.CharField(max_length=200, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Product(models.Model):
    name=models.CharField(max_length=50, null=False, blank=False)
    category_id= models.ForeignKey('Category', on_delete=models.CASCADE,blank=False, null=False )
    cost= models.IntegerField(null=False, blank=False)
    quantity= models.IntegerField(null=False, blank=False)
    description= models.TextField(null=True, blank=True)
    image=models.ImageField(upload_to='images/')
    featured=models.BooleanField(max_length=50, null=False, blank=True, default=False)
    status= models.CharField(max_length=50, null=False, blank=True, default="Unverified")
    seller_id=models.CharField(max_length=50, null=False, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Order(models.Model):
    order_number= models.CharField(max_length=100,null=False, blank=False)
    shipping_cost= models.IntegerField(null=True, blank=True)
    status= models.CharField(max_length=300, null=False, blank=False, default="Pending")
    total= models.IntegerField(null=False, blank=False)
    customer_id= models.ForeignKey('Customer', on_delete= models.CASCADE, null=False, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class OrderProduct(models.Model):
    order_id=models.ForeignKey('Order', on_delete=models.CASCADE, blank=True, null=True)    
    product_id=models.ForeignKey('Product', on_delete=models.CASCADE, null=False, blank=False)
    quantity=models.IntegerField(null=False, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Feedback(models.Model):
    message=models.TextField(null=False, blank=False)
    name=models.CharField(max_length=300, null=True, blank=True)
    email=models.EmailField(max_length=300, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Reviews(models.Model):
    rating= models.IntegerField(null=False, blank=False)
    review=models.TextField(null=True, blank=True)
    customer_id=models.ForeignKey('Customer',on_delete=models.CASCADE, null=False, blank=False)
    product_id=models.ForeignKey('Product', on_delete=models.CASCADE, null=False, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    

class Payment(models.Model):
    order_id=models.ForeignKey('Order',on_delete=models.CASCADE, null=False, blank=False)
    amount=models.IntegerField(null=False, blank=True)
    mode=models.CharField(null=False, blank=False, max_length= 300, default="Cash")
    description= models.CharField(null=True, blank=True, max_length= 500)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Delivery(models.Model):
    order_id=models.ForeignKey('Order',on_delete=models.CASCADE, null=False, blank=False)
    customer_address_id=models.ForeignKey('CustomerAddress', on_delete=models.CASCADE, blank=False, null=False )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Wishlist(models.Model):
    customer_id=models.ForeignKey('Customer',on_delete=models.CASCADE, null=False, blank=False)
    product_id= models.ForeignKey('Product',on_delete=models.CASCADE, null=False, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Offer(models.Model):
    product_id= models.ForeignKey('Product',on_delete=models.CASCADE, null=False, blank=False)
    offer_amount= models.IntegerField(null=False, blank=False)
    start_date= models.DateTimeField(null=False, blank=False)
    end_date= models.DateTimeField(null=False, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Voucher (models.Model):
    product_id= models.ForeignKey('Product',on_delete=models.CASCADE, null=False, blank=False)
    voucher_amount= models.IntegerField(null=False, blank=False)
    voucher_tag= models.CharField(null=False, blank=False, max_length= 50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
