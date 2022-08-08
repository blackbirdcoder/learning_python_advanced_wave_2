from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug_name': ['title']
    }
    list_display = 'title',


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug_name': ['title']
    }
    list_display = 'title', 'location', 'amount', 'category_id', 'category'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)