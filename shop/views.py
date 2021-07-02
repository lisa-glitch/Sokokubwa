from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Category, Seller, Product, Offer, Voucher, Order    
from django.urls import reverse
from django.http import JsonResponse

# Create your views here.


# Create your views here.
def home(request):

    context= {}

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
    model=Category
    template_name= 'shop/admin/category_list.html'

class CategoryDetail(DetailView):
    model=Category

class CategoryUpdate(UpdateView):
    model=Category
    fields=['name']
    success_url="/categories"

class CategoryDelete(DeleteView):
    model=Category

    success_url="/categories"


class SellerCreate(CreateView):
    model= Seller
    fields= ['user_name', 'email', 'logo', 'phone number', 'status', 'password']
    
    def get_success_url(self):
        return reverse('home') 


class ProductCreate(CreateView):
    model= Product
    fields=['name', 'cost', 'quantity', 'description', 'image', 'seller_id', 'category_id']


class CategoryList(ListView):
    model=Category
    template_name= 'shop/admin/category_list.html'

class ProductList(ListView):
    model=Product
    template_name= 'shop/admin/product_list.html'


class OfferList(ListView):
    model= Offer
    template_name= 'shop/admin/offer_list.html'


class VoucherList(ListView):
    model=Voucher
    template_name= 'shop/admin/voucher_list.html'


class OrderList(ListView):
    model=Order
    template_name= 'shop/admin/order_list.html'


class OrderCreate(CreateView):
    model=Order
    template= 'shop/admin/order_form.html'


def deleteCategory(request):
    category_id=request.POST.get('id', None)
    category=Category.objects.get(id=category_id)
    category.delete()
    data={
        'deleted':True
    }
    return JsonResponse(data)

