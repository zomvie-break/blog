from django.urls import path
from aboutme.views import ProfileView

app_name = 'aboutme'
urlpatterns = [
    path('', ProfileView.as_view(), name='about_me'),
]
