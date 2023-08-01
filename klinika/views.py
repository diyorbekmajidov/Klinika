from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class KlinikaApiview(APIView):
    def get(self, request):
        klinika = Kilinikalar.objects.all()
        serializer = KilinikalarSerializer(klinika, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = KilinikalarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
