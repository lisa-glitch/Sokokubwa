from django.urls import path
from . import views
from shop.views import CategoryDelete, deleteCategory, CategoryList, CategoryDetail, CategoryCreate, CategoryUpdate, ProductList, OfferList, OrderList, VoucherList

urlpatterns=[
    path("", views.home, name='home'),
    path('categories',CategoryList.as_view(), name='categories'),
    path('category/detail/<pk>/', CategoryDetail.as_view(),name='category_detail'),
    path('create/category', CategoryCreate.as_view(), name='category_create'),
    path('category/update/<pk>/', CategoryUpdate.as_view(), name='category_update'),
    path('category/delete/<pk>/',CategoryDelete.as_view(), name='category_delete'),
    path('products',ProductList.as_view(), name='product_list'),
    path('offers',OfferList.as_view(), name='offer_list'),
    path('vouchers',VoucherList.as_view(), name='voucher_list'),
    path('orders',OrderList.as_view(), name='order_list'),
    path('ajax/delete/category', views.deleteCategory, name="ajax_delete_category"),
    


]