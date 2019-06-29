from django.urls import path
from . import views

app_name = 'program'
urlpatterns = [
    path('', views.programList, name='index'),
    path('create_program', views.create_program, name='program_create'),
    path('<str:url_key>', views.program_detail, name='program_detail'),
    path('create_chapter/<str:url_key>', views.create_chapter, name='chapter_create'),
    path('create_subject/<str:url_key>/<int:pk>', views.create_subject, name='subject_create'),
]