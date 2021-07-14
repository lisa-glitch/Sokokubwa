from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from shop.views import *

urlpatterns=[
    path("", views.home, name='home'),
    path('categories',CategoryList.as_view(), name='categories'),
    path('category/detail/<pk>/', CategoryDetail.as_view(),name='category_detail'),
    path('create/category', CategoryCreate.as_view(), name='category_create'),
    path('category/update/<pk>/', CategoryUpdate.as_view(), name='category_update'),
    path('category/delete/<pk>/',CategoryDelete.as_view(), name='category_delete'),
    path('products', ProductList.as_view(), name='product_list'),
    path('product/create', ProductCreate.as_view(), name='product_form'),
    path('product/update/<pk>', ProductUpdate.as_view(), name='product_update'),
    path('offers', OfferList.as_view(), name='offer_list'),
    path('vouchers',VoucherList.as_view(), name='voucher_list'),
    path('orders',OrderList.as_view(), name='order_list'),
    path('ajax/delete/category', views.deleteCategory, name="ajax_delete_category"),
    
    


]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)