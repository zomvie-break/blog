from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.views import generic
from .models import Task
from .serializers import TaskSerializer

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# views for authentication
class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task-list')

# vies for tasks
class TaskListView(generic.ListView):
    model = Task


# APIs

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def taskList(request):
    tasks = Task.objects.all().filter(user=request.user).order_by('-id')
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def taskDetail(request,pk):
    task = Task.objects.filter(user=request.user).get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)   
    if serializer.is_valid():
        serializer.save(user=request.user)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def taskUpdate(request,pk):
    task = Task.objects.filter(user=request.user).get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
    return Response(serializer.data)

@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def taskDelete(request,pk):
    task = Task.objects.filter(user=request.user).get(id=pk)
    task.delete()
    return Response('Item successfully deleted!')