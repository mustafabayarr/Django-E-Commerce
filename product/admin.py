from django.contrib import admin

# Register your models here.
from product.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','status']
    list_filter = ['status']

admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','status','price','amount','category',]
    list_filter = ['status','category']

admin.site.register(Product,ProductAdmin) #modeli oluşturduktan sonra adminde göstermek için kullanılır.