from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from bposts.models import Posts
# Create your views here.
class PostsListView(ListView):
    model = Posts
class PostsDetailView(DetailView):
    model = Posts
