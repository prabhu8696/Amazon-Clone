from django.contrib import admin
from .models import Product, ReviewRating, Variation, ProductGallery
import admin_thumbnails


@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

@admin.register(Product)    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock','category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInline]

@admin.register(Variation) 
class VariationAdmin(admin.ModelAdmin):
    list_display  = ('product', 'variation_category', 'variation_value', 'created_date', 'is_active')
    list_editable = ('is_active',)
    list_filter   = ('product', 'variation_category', 'variation_value')

admin.site.register(ReviewRating)
admin.site.register(ProductGallery)

  