from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    # list_filter = ('author',)
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
