from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'post_tittle', 'post_author', 'post_date', 'post_category', 'post_published',)
    list_editable = ('post_published',)
    list_display_links = ('id', 'post_tittle')

admin.site.register(Post, PostAdmin)