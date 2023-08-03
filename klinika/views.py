from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class KlinikaApiview(APIView):

    @swagger_auto_schema(
        request_body = KilinikalarSerializer,
        responses={200: KilinikalarSerializer(many=True)}
    )
    def post(self, request):
        serializer = KilinikalarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        klinika = Kilinikalar.objects.all()
        serializer = KilinikalarSerializer(klinika, many=True)
        return Response(serializer.data)
    


    
class XizmatlarApiview(APIView):
    
        @swagger_auto_schema(
            request_body = XizmatlarSerializer,
            responses={200: XizmatlarSerializer(many=True)}
        )
    
        def post(self, request):
            serializer = XizmatlarSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        def get(self, request):
            xizmat = Xizmatlar.objects.all()
            serializer = XizmatlarSerializer(xizmat, many=True)
            return Response(serializer.data)
    
class ShifokorlarApiview(APIView):

    @swagger_auto_schema(
        request_body = ShifokorlarSerializer,
        responses={200: ShifokorlarSerializer(many=True)}
    )

    def post(self, request):
        serializer = ShifokorlarSerializer(data=request.data)
        xizmatlar = Xizmatlar.objects.get(id=request.data["xizmatlar"])

        if serializer.is_valid():
            serializer.save(xizmatlar=xizmatlar)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ShifokorGet(APIView):
    def get(self, request, pk):
        shifokor = Shifokorlar.objects.get(id=pk)
        serializer = ShifokorlarSerializer(shifokor)
        return Response(serializer.data)
    

class NarxlarApiview(APIView):

    @swagger_auto_schema(
        request_body = NarxlarSerializer,
        responses={200: NarxlarSerializer(many=True)}
    )

    def post(Apiview, request):
        data = request.data
        serializer = NarxlarSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        narx = Narxlar.objects.all()
        serializer = NarxlarSerializer(narx, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        request_body = NarxlarSerializer,
        responses={200: NarxlarSerializer(many=True)}
    )

    def put(self, request, pk):
        narx = Narxlar.objects.get(id=pk)
        serializer = NarxlarSerializer(instance=narx, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    
    
