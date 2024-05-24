from django.contrib import admin

from products.models import Product, Category, File


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'parent', 'title', 'is_active', 'created_time']
    list_filter = ['parent', 'is_active']
    search_fields = ['title']


class FileInlineAdmin(admin.TabularInline):
    model = File
    fields = ['id', 'title', 'file', 'is_active']
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_active', 'created_time']
    list_filter = ['is_active']
    filter_horizontal = ['category']
    inlines = [FileInlineAdmin]
