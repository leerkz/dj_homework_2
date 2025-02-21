from django.contrib import admin
from blog.models import BlogPost


# Register your models here.

@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'views_count', 'is_published')
    search_fields = ('title',)
    list_filter = ('is_published', 'created_at')
    ordering = ('created_at',)
