from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    # /board/
    path('', views.BoardList.as_view(), name='index'),
    # /board/board
    path('board/', views.BoardList.as_view(), name = 'board_list'),
    # /board/id/
    path('<int:pk>/', views.BoardDetail.as_view(), name = 'board_detail'),
    # /board/id/comment
    path('<int:pk>/comment/', views.CommentList.as_view(), name = 'comment_list'),
    # /board/new/ -> To crate new post
    path('new/', views.board_new, name = "board_new"),
    # /board/edit/ -> To edit post
    path('edit/<int:pk>/', views.board_edit, name = "board_edit")
]