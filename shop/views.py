from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Category, Seller, Product
from django.urls import reverse

# Create your views here.

class CategoryCreate(CreateView):
    model=Category
    #specify the fields to be displayed
    fields=[__all__]
    #function to redirect users
    def get_success_url(self):
        return reverse('category_list')


class SellerCreate(CreateView):
    model= Seller
    fields= ['user_name', 'email', 'logo', 'phone number', 'status', 'password']
    
    def get_success_url(self):
        return reverse('home') 


class ProductCreate(CreateView):
    model= Product
    fields=['name', 'cost', 'quantity', 'description', 'image', 'seller_id', 'category_id']


