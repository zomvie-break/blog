from django.urls import path
from bposts.views import PostsListView, PostsDetailView

urlpatterns = [
    path('posts/', PostsListView.as_view(), name='posts_list'),
    path('posts/<int:pk>/', PostsDetailView.as_view(), name='posts_list'),
]