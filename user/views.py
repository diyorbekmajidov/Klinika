from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token


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
            token = Token.objects.create(user=serializer.instance)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    permission_classes = [IsAuthenticated]
    headr_param = openapi.Parameter("Authorization", in_=openapi.IN_HEADER, description="JWT Token", type=openapi.TYPE_STRING)
    @swagger_auto_schema(manual_parameters=[headr_param])

    def post(self, request):
        user = request.user
        token =Token.objects.get_or_create(user=user)
        if token:
            token.delete()
        token = Token.objects.create(user=user)

        return Response({'token': token.key}, status=status.HTTP_200_OK)
    
class LogOut(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    @swagger_auto_schema(
        operation_description='User Logout',
        responses={
            200: 'User logged out'
        }
    )
    def post(self, request):
        request.user.auth_token.delete()
        return Response({'success': 'User logged out'})
    
