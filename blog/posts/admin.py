from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    list_display = ('id', 'post_tittle', 'post_author', 'post_date', 'post_category', 'post_published',)
    list_editable = ('post_published',)
    list_display_links = ('id', 'post_tittle')
    summernote_fields = ('post_content',)

admin.site.register(Post, PostAdmin)