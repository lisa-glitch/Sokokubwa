from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Category, Feedback, 

# Create your views here.

class CategoryCreate(CreateView):
    model=Category
    #specify the fields to be displayed
    fields=['name']
    #function to redirect users
    def get_success_url(self):
        return reverse('category_list')


class FeedbackCreate(CreateView):
    model= Feedback
    fields= {'user_name', 'message'}
    
    def get_success_url(self):
        return reverse('home') 
