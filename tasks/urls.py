from django.urls import path
from .views import *


urlpatterns = [
    path('update/<int:pk>', UpdateTask.as_view()),
    path('tasks', ListTask.as_view()),
    path('create', CreateTask.as_view()),
    path('delete/<int:pk>', DeleteTask.as_view()),
]
