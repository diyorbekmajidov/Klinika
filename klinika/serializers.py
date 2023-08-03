from rest_framework import serializers
from .models import *

class KilinikalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kilinikalar
        fields = "__all__"

class NarxlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Narxlar
        fields = ["narx", "xizmat"]

class XizmatlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xizmatlar
        fields = "__all__"

class ShifokorlarSerializer(serializers.ModelSerializer):
    xizmatlar = serializers.SerializerMethodField()

    class Meta:
        model = Shifokorlar
        fields = ["id", "name", "qavat", "xizmatlar", "ish_kunlari", "info", "img", "ish_vaqt"]

    def get_xizmatlar(self, obj):
        return obj.xizmatlar.name
    

class NavbatlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Navbatlar
        fields = "__all__"
        