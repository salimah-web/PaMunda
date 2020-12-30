from django.contrib import admin
from .models import Product,Make_order,Category
# Register your models here.

admin.site.register(Product)
admin.site.register(Make_order)
admin.site.register(Category)