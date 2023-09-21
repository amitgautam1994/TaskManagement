from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *


# CRUD Operations

class ListTask(generics.ListAPIView):  # Read
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UpdateTask(generics.RetrieveUpdateAPIView):  # Update
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CreateTask(generics.CreateAPIView):  # Create
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class DeleteTask(generics.DestroyAPIView):  # Delete
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
