from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin

from product.models import Category, Product, Images

#product tablosuna Images modelini ekledik.
class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5

class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'

admin.site.register(Category,CategoryAdmin2)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','status','price','amount','category','image_tag']
    list_filter = ['status','category']
    inlines = [ProductImageInline]  #Image modelini aktif ettik
    readonly_fields = ['image_tag']

admin.site.register(Product,ProductAdmin) #modeli oluşturduktan sonra adminde göstermek için kullanılır.

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','product','image_tag']
    readonly_fields = ['image_tag']
admin.site.register(Images,ImagesAdmin)