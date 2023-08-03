from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password


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

class XizmatlarGet(APIView):
        """
        Xizmatlar get by id and xizmatlar malumotlari
        """

        def get(self, request, pk):
            xizmat = Xizmatlar.objects.get(id=pk)
            serializer = XizmatlarSerializer(xizmat)
            return Response(serializer.data)
    

class ShifokorlarApiview(APIView):

    @swagger_auto_schema(
        request_body = ShifokorlarSerializer,
        responses={200: ShifokorlarSerializer(many=True)}
    )

    def post(self, request):
        data = request.data
        data["password"] = make_password(data["password"])
        serializer = ShifokorlarSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        shifokor = Shifokorlar.objects.all()
        serializer = ShifokorlarSerializer(shifokor, many=True)
        return Response(serializer.data)
    

class ShifokorGet(APIView):
    """
    Shifokor get by id and shifokor malumotlari
    """

    @swagger_auto_schema(
        responses={200: ShifokorlarSerializer(many=True)}
    )

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
    
class NarxlarGet(APIView):
    """
    Narxlar get by id and narxlar malumotlari
    """

    @swagger_auto_schema(
        responses={200: NarxlarSerializer(many=True)}
    )

    def get(self, request, pk):
        narx = Narxlar.objects.get(id=pk)
        serializer = NarxlarSerializer(narx)
        return Response(serializer.data)
    
    
    
class NavbatApiview(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    """
    Bemor uchun navbat yaratish uchun api
    """
    @swagger_auto_schema(
        request_body = NavbatlarSerializer,
        responses={200: NavbatlarSerializer(many=True)}
    )

    def post(self, request):
        navbat = Navbatlar.objects.all()
        data = request.data
        data["navbat_raqam"] = navbat.count() + 1
        serializer = NavbatlarSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

# class ShifokorCabenit(APIView):

#     def get(self, request):
#         shi
