from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.

from .models import User
from .serializers import UserSerializer

class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        item = self.request.query_params.get("item", "")

        if item !="":
            users = users.filter(name=item)

        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPIView(APIView):

    def get(self, request, user_id):
        user = get_object_or404(User, id=user_id)
        serializer = UserSerializer(user)
        return Response(data=serializer.data)
