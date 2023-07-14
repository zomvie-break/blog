from django.urls import path
from .views import TaskListView
from .views import taskList, taskDetail, taskCreate, taskUpdate, taskDelete

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
]

# API
urlpatterns += [
    path('api/task-list/', taskList, name="api-task-list"),
    path('api/task-item/<int:pk>/', taskDetail, name="api-task-detail"),
    path('api/task-create/', taskCreate, name="api-task-create"),
    path('api/task-update/<int:pk>/', taskUpdate, name="api-task-update"),
    path('api/task-delete/<int:pk>/', taskDelete, name="api-task-delete"),
]