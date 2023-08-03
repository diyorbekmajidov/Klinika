from rest_framework import serializers
from .models import *

class KilinikalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kilinikalar
        fields = "__all__"

class XizmatlarSerializer(serializers.ModelSerializer):
    klinika = serializers.SerializerMethodField()
    class Meta:
        model = Xizmatlar
        fields = ["id", "name","klinika"]

    def get_klinika(self, obj):
        return obj.klinika.name

class NarxlarSerializer(serializers.ModelSerializer):
    xizmat = serializers.SerializerMethodField()

    class Meta:
        model = Narxlar
        fields = ["narx", "xizmat","id"]

    def get_xizmat(self, obj):
        return obj.xizmat.name


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
        