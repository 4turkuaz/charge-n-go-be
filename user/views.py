from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserEntity
from .serializers import UserSerializer, CredentialSerializer


class Users(APIView):
    """
    List all users, or create a new user
    """

    def get(self, request):
        all_users = UserEntity.objects.all()
        serializer = UserSerializer(all_users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetails(APIView):
    """
    Retrieve & Update & Delete operations for a User instance.
    """

    def _get_user(self, pk):
        return get_object_or_404(UserEntity, pk=pk)

    def get(self, request, pk):
        user = self._get_user(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Update user with primary key pk
        """
        user = self._get_user(pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self._get_user(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Login(APIView):
    def post(self, request):
        """
        Returns true if user is authenticated false otherwise
        """
        serializer = CredentialSerializer(data=request.data)
        return Response(data=serializer.is_valid())
