from django.urls import path
from bposts.views import PostsListView, PostsDetailView

app_name = 'bposts'
urlpatterns = [
    path('posts/', PostsListView.as_view(), name='posts_list'),
    path('posts/<int:pk>/', PostsDetailView.as_view(), name='posts_detail'),
]