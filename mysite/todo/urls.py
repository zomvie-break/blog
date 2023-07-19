from django.urls import path
from .views import TaskListView
from .views import taskList, taskDetail, taskCreate, taskUpdate, taskDelete
from .views import CustomLoginView, CustomLogoutView, RegisterView

app_name = "todo-list"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),

]

# API
urlpatterns += [
    path('api/task-list/', taskList, name="api-task-list"),
    path('api/task-item/<int:pk>/', taskDetail, name="api-task-detail"),
    path('api/task-create/', taskCreate, name="api-task-create"),
    path('api/task-update/<int:pk>/', taskUpdate, name="api-task-update"),
    path('api/task-delete/<int:pk>/', taskDelete, name="api-task-delete"),
]
