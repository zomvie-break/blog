from django.shortcuts import render
from django.views import View
from myprojects.models import Project
from bposts.models import Posts

# Create your views here.

class MainView(View):
    template_name='home/index.html'
    def get(self, request):
        projects = Project.objects.all()
        posts = Posts.objects.all()
        context = {'projects':projects, 'posts':posts}
        return render(request, self.template_name, context)
