from django.contrib import admin
from reviews.models import Product, Category, ProductSize, Company, ProductSite, Comment

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'content']
    list_filter = ['category',]

admin.site.register(Category)
admin.site.register(ProductSize)
admin.site.register(Comment)
admin.site.register(Company)
admin.site.register(ProductSite)


