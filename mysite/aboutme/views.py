from django.shortcuts import render
from django.views.generic import TemplateView
from aboutme.models import Profile

# Create your views here.
class ProfileView(TemplateView):
    template_name = 'aboutme/about_me.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context["profiles"] = Profile.objects.all()
        return context
    