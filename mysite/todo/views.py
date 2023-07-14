from django.shortcuts import render
from django.views import generic
from .models import Task
from .serializers import TaskSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
class TaskListView(generic.ListView):
    model = Task


# APIs
@api_view(['GET'])
def get_all_tasks(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_task(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)