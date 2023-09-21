from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import UserSerializer

from .serializers import *
from .models import *


# Authentication


class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = serializer.instance
        response_data = {
            "username": user.username,
            "email": user.email
        }
        return Response(response_data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            serializer = UserSerializer(user)
            refresh = RefreshToken.for_user(user)
            return Response({
                "token": str(refresh.access_token),
                "refresh_token": str(refresh),
                "username": serializer.data['username'],
                "email": serializer.data['email']
            })
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get('refresh_token')

        if refresh_token:
            # try:
            token = RefreshToken(refresh_token)
            print(token)
            token.blacklist()
            return Response({"message": "Logout successful."}, status=status.HTTP_200_OK)
            # except TokenError:
            #     return Response({"error": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)


# CRUD Operations

class ListTask(generics.ListAPIView):  # Read
    permission_classes = (IsAuthenticated,)
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
