from rest_framework import serializers
from .models import Penulis, Kategori, Buku

class PenulisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Penulis
        fields = '__all__'

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'

class BukuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buku
        fields = '__all__'
