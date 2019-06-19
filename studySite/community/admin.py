from django.contrib import admin
from .models import Community, Post, Comment

# Register your models here.

class CommunityAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id']

admin.site.register(Community)
admin.site.register(Post)
admin.site.register(Comment)
