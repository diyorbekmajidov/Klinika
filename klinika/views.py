from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

class KilinikarViewSet(viewsets.ModelViewSet):
    queryset = Kilinikalar.objects.all()
    serializer_class = KilinikalarSerializer

    def list(self, request):
        queryset = Kilinikalar.objects.all()
        serializer = KilinikalarSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = KilinikalarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def update(self, request, pk=None):
        queryset = Kilinikalar.objects.all()
        kilinikalar = get_object_or_404(queryset, pk=pk)
        serializer = KilinikalarSerializer(kilinikalar, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def destroy(self, request, pk=None):
        queryset = Kilinikalar.objects.all()
        kilinikalar = get_object_or_404(queryset, pk=pk)
        kilinikalar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
