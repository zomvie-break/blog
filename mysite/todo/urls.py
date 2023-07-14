from django.urls import path
from .views import TaskListView
from .views import get_all_tasks, get_task

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
]

# API
urlpatterns += [
    path('api/task-list/', get_all_tasks, name="get-task-list"),
    path('api/task-item/<int:pk>/', get_task, name="get-task-list"),
    
]
