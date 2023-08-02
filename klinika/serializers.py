from rest_framework import serializers
from .models import *

class KilinikalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kilinikalar
        fields = "__all__"

class NarxlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Narxlar
        fields = "__all__"

class XizmatlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xizmatlar
        fields = "__all__"

class ShifokorlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shifokorlar
        fields = "__all__"

class NavbatlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Navbatlar
        fields = "__all__"
        