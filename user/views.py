from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.hashers import make_password

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class Register(APIView):
    @swagger_auto_schema(
        request_body = UserSerializer,
        responses={200: UserSerializer(many=True)}
    )
    def post(self,requests):
        serializer = UserSerializer(data=requests.data)
        if serializer.is_valid():
            serializer.save(password=make_password(serializer.validated_data['phone_number']))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
