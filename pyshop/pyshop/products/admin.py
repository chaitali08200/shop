from django.contrib import admin
from . models import Products
from .models import Offer

class ProductsAdmin(admin.ModelAdmin):
    list_display=('name', 'price', 'stock')
admin.site.register(Products, ProductsAdmin)

class OfferAdmin(admin.ModelAdmin):
    list_display=('code', 'description','discount')
admin.site.register(Offer, OfferAdmin)