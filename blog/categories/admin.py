from .models import Category
from django.contrib import admin

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat_name')
    list_display_links = ('id', 'cat_name')

admin.site.register(Category, CategoryAdmin)