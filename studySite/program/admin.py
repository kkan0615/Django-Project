from django.contrib import admin
from .models import Code, Program, Subject, Subject_comment, Chapter

# Register your models here.

class CodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class ProgramAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

class ChpaterAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

class Subject_commentAdmin(admin.ModelAdmin):
    list_display = ['id']

admin.site.register(Code)
admin.site.register(Program)
admin.site.register(Chapter)
admin.site.register(Subject)
admin.site.register(Subject_comment)
