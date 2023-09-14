from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class WeightIndexView(TemplateView):
    template_name = "weight/weight_sample.html"

class WeightUserView(LoginRequiredMixin, TemplateView):
    template_name = "weight/weight_user.html"