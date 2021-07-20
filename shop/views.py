from django.shortcuts import render
from django.views.generic.edit import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Category, Customer, Payment, Seller, Product, Offer, Voucher, Order    
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
        return reverse('categories')


class CategoryList(ListView):
    login_required=True
    model=Category
    template_name= 'shop/admin/category_list.html'
    

class CategoryDetail(DetailView):
    login_required=True
    model=Category
    fields='--all--'
    template_name='shop/admin/category_detail.html'

class CategoryUpdate(UpdateView):
    login_required=True
    model=Category
    fields=['name']
    template_name="shop/admin/category_update.html"
    success_url="/categories"


    

class SellerCreate(CreateView):
    login_required=True
    model= Seller
    fields= ['email', 'logo', 'phone_number', 'status', 'password']
    template_name="shop/admin/seller_form.html"

    def get_success_url(self):
        return reverse('seller_list') 


class SellerList(ListView):
    login_required=True
    model= Seller
    fields= ['email', 'logo', 'phone_number', 'status', 'password']
    template_name=('shop/admin/seller_list.html')


class SellerUpdate(UpdateView):
    login_required=True
    model= Seller
    fields= ['email', 'logo', 'phone_number', 'status', 'password']
    template_name= 'shop/admin/seller_update.html'

    def get_success_url(self):
        return reverse('seller_list') 


class SellerDelete(DeleteView):
    login_required=True
    model= Seller
    fields= ['email', 'logo', 'phone_number', 'status', 'password']
    template_name= 'shop/admin/seller_delete.html'

    def get_success_url(self):
        return reverse('seller_list') 

class SellerDetail(DetailView):
    login_required=True
    model= Seller
    fields= ['email', 'logo', 'phone_number', 'status', 'password']
    template_name='shop/admin/seller_detail.html'



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
    template_name='shop/admin/product_update.html'

    def get_success_url(self):
        return reverse('product_list')


class ProductDelete(DeleteView):
    login_required=True
    model= Product
    fields= ['name', 'cost', 'quantity', 'description', 'image', 'seller_id', 'category_id']
    template_name='shop/admin/product_delete.html'
    def get_success_url(self):
        return reverse('product_list') 


class ProductDetail(DetailView):
    login_required=True
    model= Product
    fields= ['name', 'cost', 'quantity', 'description', 'image', 'seller_id', 'category_id']
    template_name='shop/admin/product_detail.html'
    


class ProductList(ListView):
    login_required=True
    model=Product
    fields= ['name', 'cost', 'quantity', 'description', 'image', 'seller_id', 'category_id']
    template_name= 'shop/admin/product_list.html' 



class OfferCreate(CreateView):
    login_required= True
    model= Offer
    fields= ['product_id', 'offer_amount','start_date', 'end_date']
    template_name= 'shop/admin/offer_list.html'

    def get_success_url(self):
        return reverse('offer_list')

class OfferList(ListView):
    login_required= True
    model= Offer
    fields= ['product_id', 'offer_amount','start_date', 'end_date']
    template_name= 'offer_list'

class OfferDetail(DetailView):
    login_required=True
    model=Offer
    fields= ['product_id', 'offer_amount','start_date', 'end_date']
    template_name='shop/admin/offer_detail.html'

class OfferDelete(DeleteView):
    login_required=True
    model=Offer
    fields= ['product_id', 'offer_amount','start_date', 'end_date']
    template_name='shop/admin/offer_delete.html'

class OfferUpdate(UpdateView):
    login_required=True
    model=Offer
    fields= ['product_id', 'offer_amount','start_date', 'end_date']
    template_name='shop/admin/offer_update_html'

    def get_success_url(self):
        return reverse ('offer_list')



class VoucherCreate(CreateView):
    template_name='shop/admin/voucher_form.html'
    model=Voucher
    login_required=True
    fields=['product_id', 'voucher_amount', 'voucher_tag']
    success_url="/vouchers"


class VoucherList(ListView):
    login_required=True
    model=Voucher
    fields=['product_id', 'voucher_amount', 'voucher_tag']
    template_name= 'shop/admin/voucher_list.html'
    
class VoucherDetail(DetailView):
    login_required=True
    model=Voucher
    fields=['product_id', 'voucher_amount', 'voucher_tag']
    template_name= 'shop/admin/voucher_detail.html'

class VoucherUpdate(UpdateView):
    login_required=True
    template_name='shop/admin/voucher_update.html'
    fields=['product_id', 'voucher_amount', 'voucher_tag']
    model=Voucher
    success_url='/vouchers'

class VoucherDelete(DeleteView):
    login_required=True
    fields=['product_id', 'voucher_amount', 'voucher_tag']
    template_name='/shop/admin/voucher_delete.html'
    success_url='/vouchers'



class OrderCreate(CreateView):
    login_required=True
    model=Order
    fields=['order_number', 'shipping_cost', 'status', 'total', 'customer_id']
    template_name= 'shop/admin/order_form.html'
    success_url='/orders'


class OrderList(ListView):
    login_required=True
    model=Order
    fields=['order_number', 'shipping_cost', 'status', 'total', 'customer_id']
    template_name= 'shop/admin/order_list.html'

class OrderDetail(DetailView):
    login_required=True
    fields=['order_number', 'shipping_cost', 'status', 'total', 'customer_id']
    model=Order
    template_name= 'shop/admin/order_detail.html'


class OrderUpdate(UpdateView):
    login_required=True
    model=Order
    fields=['order_number', 'shipping_cost', 'status', 'total', 'customer_id']
    template_name= 'shop/admin/order_update.html'
    success_url='/orders'

class OrderDelete(DeleteView):
    login_required=True
    model=Order
    fields=['order_number', 'shipping_cost', 'status', 'total', 'customer_id']
    template_name= 'shop/admin/order_delete.html'
    success_url='/orders'

@login_required
def deleteCategory(request):
    category_id=request.POST.get('id', None)
    category=Category.objects.get(id=category_id)
    category.delete()

    ##If the category is deleted successfully
    ##Send a confirmation message to the frontend
    ##Response messages are usually sent as dictionaries
    ##Here we are sending a message boolean of true
    data={
        'deleted':True
    }
    return JsonResponse(data)



class CustomerCreate(CreateView):
    login_required=True
    model=Customer
    fields=['name', 'email', 'password', 'phone_number']
    template_name= 'shop/admin/customer_form.html'
    success_url='/customer'

class CustomerList(ListView):
    login_required=True
    fields=['name', 'email', 'password', 'phone_number']
    model=Customer
    template_name='shop/admin/customer_list.html'

class CustomerDetail(DetailView):
    template_name= 'shop,admin/customer_detail.html'
    login_required=True
    fields=['name', 'email', 'password', 'phone_number']
    success_url='/customer'

class CustomerUpdate(UpdateView):
    template_name= 'shop,admin/customer_update.html'
    login_required=True
    fields=['name', 'email', 'password', 'phone_number']
    success_url='/customer'


class CustomerDelete(DeleteView):
    login_required=True
    model=Customer
    fields=['name', 'email', 'password', 'phone_number']
    template_name='shop/admin/customer_delete.html'
    success_url='/customer'



class PaymentCreate(CreateView):
    login_required=True
    fields=['order_id', 'mode', 'amount', 'description']
    model=Payment
    template_name='shop/admin/payment_form.html'
    success_url='/payment'

class PaymentList(ListView):
    login_required=True
    fields=['order_id', 'mode', 'amount', 'description']
    model=Payment
    template_name='shop/admin/payment_list.html'

class PaymentDetail(DetailView):
    login_required=True
    fields=['order_id', 'mode', 'amount', 'description']
    model=Payment
    template_name='shop/admin/payment_detail.html'


class PaymentUpdate(UpdateView):
    login_required=True
    model=Payment
    fields=['order_id', 'mode', 'amount', 'description']
    template_name='shop/admin/payment_update.html'
    success_url='/payment'

class PaymentDelete(DeleteView):
    login_required=True
    model=Payment
    fields=['order_id', 'mode', 'amount', 'description']
    template_name='shop/admin/payment_delete.html'
    success_url='/payment'