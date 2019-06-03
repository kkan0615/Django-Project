from django.contrib import admin
from .models import Board, Comment, Like

class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

admin.site.register(Board)
admin.site.register(Comment)
admin.site.register(Like)