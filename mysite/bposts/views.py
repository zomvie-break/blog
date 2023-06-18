from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from bposts.models import Posts, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from bposts.forms import CommentForm 

from home.owner import OwnerListView, OwnerDetailView, OwnerCreateView
# Create your views here.
class PostsListView(OwnerListView):
    model = Posts
class PostsDetailView(OwnerDetailView):
    model = Posts
    template_name = 'bposts/posts_detail.html'
    def get(self, request, pk):
        ps = Posts.objects.get(id=pk)
        comments = ps.comment.all().order_by('-modified_at')
        comment_form = CommentForm()
        context = {'object':ps, 'comments':comments, 'comment_form':comment_form}
        return render(request, self.template_name, context) 
        
class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        p = get_object_or_404(Posts, id=pk)
        comment = Comment(content=request.POST['comment'], creator=request.user, content_object=p)
        comment.save()
        return redirect(reverse('bposts:posts_detail', args=[pk]))
