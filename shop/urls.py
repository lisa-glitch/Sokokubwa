from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from shop.views import *

urlpatterns=[
    path("", views.home, name='home'),
    path('dashboard', views.adminDashboard, name='dashboard'),
    path('categories',CategoryList.as_view(), name='categories'),
    path('category/detail/<pk>/', CategoryDetail.as_view(),name='category_detail'),
    path('create/category', CategoryCreate.as_view(), name='category_create'),
    path('category/update/<pk>/', CategoryUpdate.as_view(), name='category_update'),
    path('ajax/delete/category', views.deleteCategory, name="ajax_delete_category"),

    path('products', ProductList.as_view(), name='product_list'),
    path('product/create', ProductCreate.as_view(), name='product_form'),
    path('product/detail/<pk>/', ProductDetail.as_view(), name='product_detail'),
    path('product/update/<pk>/', ProductUpdate.as_view(), name='product_update'),
    path('product/delete/<pk>/', ProductDetail.as_view(), name='product_delete'),

    path('sellers', SellerList.as_view(), name='seller_list'),
    path('seller/create', SellerCreate.as_view(), name='seller_create'),
    path('seller/detail/<pk>/', SellerDetail.as_view(), name='seller_detail'),
    path('seller/update/<pk>/', SellerUpdate.as_view(), name='seller_update'),
    path('seller/delete/<pk>/', SellerDelete.as_view(), name='seller_delete'),
    

    path('offers', OfferList.as_view(), name='offer_list'),
    path('offer/create', OfferCreate.as_view(), name='offer_form'),
    path('offer/detail/<pk>/', OfferDetail.as_view(), name='offer_detail'),
    path('offer/update/<pk>/', OfferUpdate.as_view(), name='offer_update'),
    path('offer/delete/<pk>/', OfferDelete.as_view(), name='offer_delete'),

    path('vouchers',VoucherList.as_view(), name='voucher_list'),
    path('voucher/create', VoucherCreate.as_view(), name='voucher_form'),
    path('voucher/detail/<pk>/', VoucherDetail.as_view(), name='voucher_detail'),
    path('voucher/update/<pk>/', VoucherUpdate.as_view(), name='voucher_update'),
    path('voucher/delete/<pk>/', VoucherDelete.as_view(), name='voucher_delete'),


    path('orders',OrderList.as_view(), name='order_list'),
    path('order/create', OrderCreate.as_view(), name='order_form'),
    path('order/detail/<pk>/', OrderDetail.as_view(), name='order_detail'),
    path('order/update/<pk>/', OrderUpdate.as_view(), name='order_update'),
    path('order/delete/<pk>/', OrderDelete.as_view(), name='order_delete'),

    
    path('customers', CustomerList.as_view(), name='customer_list'),
    path('customer/create', CustomerCreate.as_view(), name='customer_form'),
    path('customer/create/<pk>/', CustomerUpdate.as_view(), name='customer_update'),
    path('customer/detail/<pk>/', CustomerDetail.as_view(), name='customer_detail'),
    path('customer/delete/<pk>/', CustomerDelete.as_view(), name='customer_delete'),

    path('payments', PaymentList.as_view(), name='payment_list'),
    path('payment/create', PaymentCreate.as_view(), name='payment_form'),
    path('payment/detail/<pk>/', PaymentDetail.as_view(), name='payment_detail'),
    path('payment/update/<pk>/', PaymentUpdate.as_view(), name='payment_update'),
    path('payment/delete/<pk>/', PaymentDelete.as_view(), name='payment_delete'),

    


]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)