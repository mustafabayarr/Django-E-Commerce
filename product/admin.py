from django.contrib import admin

# Register your models here.
from product.models import Category, Product, Images

#product tablosuna Images modelini ekledik.
class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','status']
    list_filter = ['status']

admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','status','price','amount','category',]
    list_filter = ['status','category']
    inlines = [ProductImageInline]  #Image modelini aktif ettik

admin.site.register(Product,ProductAdmin) #modeli oluşturduktan sonra adminde göstermek için kullanılır.

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','product','image']

admin.site.register(Images,ImagesAdmin)