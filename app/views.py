# coding: utf-8
import logging

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ToDo
from .serializers import ToDoSerializer

log = logging.getLogger(__name__)


class ToDoApp(APIView):
    """
    To Do REST APIView
    """

    def get(self, request):
        todo_lists = ToDo.objects.all()
        serializer = ToDoSerializer(todo_lists, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        todo = ToDo.objects.get(pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def start_page(request, title="Simple Django RESTFull ToDo App"):
    """Home page view"""
    content = {'title': title}
    return render(request, 'index.html', content)
