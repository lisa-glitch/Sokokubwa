from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(Category)
admin.site.register(Admin)
admin.site.register(Customer)
admin.site.register(Seller)
admin.site.register(CustomerAddress)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Feedback)
admin.site.register(Reviews)
admin.site.register(Payment)
admin.site.register(Delivery)
admin.site.register(Wishlist)
admin.site.register(Offer)
admin.site.register(Voucher)



