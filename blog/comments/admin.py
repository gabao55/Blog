from django.contrib import admin
from .models import Comments

# Register your models here.
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment_name', 
    'comment_email', 'post_comment', 
    'comment_date', 'comment_published')
    list_editable = ('comment_published',)
    list_display_links = ('id', 'comment_name', 'comment_email',)

admin.site.register(Comments, CommentsAdmin)