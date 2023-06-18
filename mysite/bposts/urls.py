from django.urls import path
from bposts.views import PostsListView, PostsDetailView, CommentCreateView

app_name = 'bposts'
urlpatterns = [
    path('posts/', PostsListView.as_view(), name='posts_list'),
    path('posts/<int:pk>/', PostsDetailView.as_view(), name='posts_detail'),
    path('posts/<int:pk>/comment', CommentCreateView.as_view(), name='posts_comment_create'),
]