from django.contrib import admin
from .models import Post, Comment
# Register your models here.

admin.site.register(Post)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'text', 'created_date')
    list_filter = ('post', 'created_date')
    search_fields = ('text',)
