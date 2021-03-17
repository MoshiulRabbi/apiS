from rest_framework import serializers
from todo_rest.models import Task
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TaskSerializer

from .models import Task


# Create your views here.

@api_view(['GET'])
def overview(request):
    api_urls = {
        'List':'/task-list/',
        'Detail View': '/tast-detail/<str:pk>/',
        'Create': '/tast-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/'
    }

    return Response(api_urls)




@api_view(['GET'])
def tasklist(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks,many=True)
    return Response(serializer.data)



@api_view(['GET'])
def taskdetail(request,pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks,many=False)
    return Response(serializer.data)