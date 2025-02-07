from modulefinder import Module
from django.contrib import admin
from.model.Product import Product
from.model.category import Category
from.model.customer import Customer
from.model.orders import Order

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)