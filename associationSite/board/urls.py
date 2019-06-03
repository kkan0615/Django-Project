from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    # /board/
    path('', views.BoardList.as_view(), name='index'),
    # /board/board
    path('<int:page>/', views.BoardList.as_view(), name = 'board_list'),
    # /board/id/
    path('board/<int:pk>/', views.BoardDetail.as_view(), name = 'board_detail'),
    # /board/new/ -> To crate new post
    path('new/', views.board_new, name = "board_new"),
    # /board/edit/:id -> To edit post
    path('edit/<int:pk>/', views.board_edit, name = "board_edit"),
    # board/remove:id -> To remove board
    path('board/remove/<int:pk>', views.board_remove, name="board_remove"),
    # /board/comment/id/
    path('comment/<int:board_pk>', views.comment_new, name = 'comment_new'),
    # /board/comment/id/remove/id
    path('comment/<int:board_pk>/remove/<int:comment_pk>', views.comment_remove, name = 'comment_remove'),
    # /board/like
    #path('like/', views.board_like, name='board_like'),
]