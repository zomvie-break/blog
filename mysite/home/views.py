from django.shortcuts import render
from django.views import View

# Create your views here.

class MainView(View):
    template_name='home/main.html'
    def get(self, request):
        title = 'This is my blog'
        context = {'title':title}
        return render(request, self.template_name, context)
