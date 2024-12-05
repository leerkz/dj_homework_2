from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('id', 'name', 'cost', 'category',)
    search_fields = ('name', 'description',)
    list_filter = ('category',)


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name', 'description',)