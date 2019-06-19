from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('', views.CommunityList.as_view(), name='index'),
    path('posts/page/<int:page>/', views.LatestView.as_view(), name='posts'),
    path('create_new_community/', views.CreateNewCommunity, name='create_new_community'),
    path('<str:url_key>', views.CommunityDetail, name='community_detail'),
    path('<str:url_key>/post/write/', views.write_post, name='post_write'),
    path('post/<int:pk>', views.PostDetail, name='post_detail'),
]