from django.contrib import admin

from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('text', 'created', 'author')
    search_fields = ('text',)
    list_filter = ('created',)


admin.site.register(Blog, BlogAdmin)
