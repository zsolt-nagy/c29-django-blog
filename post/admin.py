from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'content', 'publish_date')


admin.site.register(Post, PostAdmin)
