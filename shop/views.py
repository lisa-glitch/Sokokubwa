from django.shortcuts import render
from django.views.generic.edit import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Category, Seller, Product, Offer, Voucher, Order    
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


# Create your views here.
def home(request):

    context = {}

    context['products']= Product.objects.all()[:4]
    context['categories']=Category.objects.all()

    return render(request, "shop/frontend/home.html", context)

class CategoryCreate(CreateView):
    model=Category
    #specify the fields to be displayed
    fields='__all__'
    template_name= 'shop/admin/category_form.html'
    #function to redirect users
    def get_success_url(self):
        return reverse('category_list')


class CategoryList(ListView):
    login_required=True
    model=Category
    template_name= 'shop/admin/category_list.html'

class CategoryDetail(DetailView):
    login_required=True
    model=Category
    login_required=True

class CategoryUpdate(UpdateView):
    login_required=True
    model=Category
    fields=['name']
    success_url="/categories"

class CategoryDelete(DeleteView):
    model=Category
    login_required=True
    success_url="/categories"


class SellerCreate(CreateView):
    login_required=True
    model= Seller
    fields= ['user_name', 'email', 'logo', 'phone number', 'status', 'password']
    
    def get_success_url(self):
        return reverse('seller_form') 


class SellerList(ListView):
    login_required=True
    model= Seller
    fields= ['user_name', 'email', 'logo', 'phone number', 'status', 'password']
    
    def get_success_url(self):
        return reverse('shop/admin/seller_list.html') 


class SellerUpdate(UpdateView):
    login_required=True
    model= Seller
    fields= ['user_name', 'email', 'logo', 'phone number', 'status', 'password']
    
    def get_success_url(self):
        return reverse('shop/admin/seller_update.html') 


class SellerDelete(DeleteView):
    login_required=True
    model= Seller
    fields= ['user_name', 'email', 'logo', 'phone number', 'status', 'password']
    
    def get_success_url(self):
        return reverse('shop/admin/seller_delete.html') 

class SellerDetail(DetailView):
    login_required=True
    model= Seller
    fields= ['user_name', 'email', 'logo', 'phone number', 'status', 'password']
    
    def get_success_url(self):
        return reverse('shop/admin/seller_detail.html') 


class ProductCreate(CreateView):
    model= Product
    fields=['name', 'cost', 'quantity', 'description', 'image', 'seller_id', 'category_id']
    template_name='shop/admin/product_form.html'
    login_required=True

    def get_success_url(self):
        return reverse('product_list')

class ProductUpdate(UpdateView):
    login_required=True
    model= Product
    fields=['name', 'cost', 'quantity', 'description', 'image', 'seller_id', 'category_id']
    template_name='shop/admin/product_form.html'

    def get_success_url(self):
        return reverse('product_list')


class ProductDelete(DeleteView):
    login_required=True
    model= Product
    fields= ['name', 'cost', 'quantity', 'description', 'image', 'seller_id', 'category_id']
    
    def get_success_url(self):
        return reverse('shop/admin/product_delete.html') 


class ProductDetail(DetailView):
    login_required=True
    model= Product
    fields= ['name', 'cost', 'quantity', 'description', 'image', 'seller_id', 'category_id']
    
    def get_success_url(self):
        return reverse('shop/admin/Product_delete.html')


class ProductList(ListView):
    login_required=True
    model=Product
    template_name= 'product_list' 


class OfferList(ListView):
    login_required=True
    model= Offer
    template_name= 'shop/admin/offer_list.html'


class VoucherList(ListView):
    login_required=True
    model=Voucher
    template_name= 'shop/admin/voucher_list.html'


class OrderList(ListView):
    login_required=True
    model=Order
    template_name= 'shop/admin/order_list.html'


class OrderCreate(CreateView):
    login_required=True
    model=Order
    template= 'shop/admin/order_form.html'

@login_required
def deleteCategory(request):
    category_id=request.POST.get('id', None)
    category=Category.objects.get(id=category_id)
    category.delete()
    data={
        'deleted':True
    }
    return JsonResponse(data)

