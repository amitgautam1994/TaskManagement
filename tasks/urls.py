from django.urls import path
from .views import *


urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', CreateTask.as_view()),
    path('tasks/', ListTask.as_view()),
    path('task_detail/<int:pk>', TaskById.as_view()),
    path('update/<int:pk>', UpdateTask.as_view()),
    path('delete/<int:pk>', DeleteTask.as_view()),
]
