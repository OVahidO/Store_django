from django.contrib import admin
from django.db.models import Count
from . import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'invetory_status']
    list_editable = ['unit_price']
    list_per_page = 20

    @admin.display(ordering='invetory')
    def invetory_status(self, product):
        if product.invetory < 10:
            return 'Low'
        return 'Ok'

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'product_count']

    def product_count(self, collection):
        return collection.product_count
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            product_count = Count('product')
        )

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['first_name', 'last_name']

# Register your models here.
# admin.site.register(models.Customer)

# admin.site.register(models.Product, ProductAdmin)