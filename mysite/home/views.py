from django.shortcuts import render
from django.views import View
from .models import Homepage

# Create your views here.

class MainView(View):
    template_name='home/index.html'
    def get(self, request):
        homepage = Homepage.objects.get(id=1)
        context = {'object':homepage}
        return render(request, self.template_name, context) 
