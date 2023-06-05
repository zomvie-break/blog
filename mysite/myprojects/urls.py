from django.urls import path
from myprojects.views import ProjectListView

app_name='myprojects'
urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
]
