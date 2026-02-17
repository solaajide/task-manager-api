from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, APIView
from .serializers import TaskSerializer
from .models import Task
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class TaskListCreateView(APIView):
    serializer_class = TaskSerializer
    
    def get(self, request:Request, *args, **kwargs):
        tasks = Task.objects.all()
        serializer = self.serializer_class(instance=tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request:Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'data':serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TaskRetrieveUpdateDeleteView(APIView):
    serializer_class = TaskSerializer
    
    def get(self, request:Request, id=int):
        task = get_object_or_404(Task, id=id)
        serializer = self.serializer_class(instance=task)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request:Request, id=int):
        task = get_object_or_404(Task, id=id)
        serializer = self.serializer_class(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request:Request, id=int):
        task = get_object_or_404(Task, id=id)
        task.delete()
        response = {
            'data':'Task Deleted'
        }
        return Response(response, status=status.HTTP_200_OK)