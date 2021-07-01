from django.urls import path
from . import views
from shop.views import CategoryDelete, CategoryList, CategoryDetail, CategoryCreate, CategoryUpdate

urlpatterns=[
    path("", views.home, name='home'),
    path('categories',CategoryList.as_view(), name='category_list'),
    path('category/detail/<pk>/', CategoryDetail.as_view(),name='category_detail'),
    path('create/category', CategoryCreate.as_view(), name='category_create'),
    path('category/update/<pk>/', CategoryUpdate.as_view(), name='category_update'),
    path('category/delete/<pk>/',CategoryDelete.as_view(), name='category_delete'),

]