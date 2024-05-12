from rest_framework import generics
from .models import Penulis, Kategori, Buku
from .serializers import PenulisSerializer, KategoriSerializer, BukuSerializer

class PenulisListView(generics.ListAPIView):
    queryset = Penulis.objects.all()
    serializer_class = PenulisSerializer

class PenulisDetailView(generics.RetrieveAPIView):
    queryset = Penulis.objects.all()
    serializer_class = PenulisSerializer
    lookup_field = 'pk'

class KategoriListView(generics.ListAPIView):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer

class KategoriDetailView(generics.RetrieveAPIView):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer
    lookup_field
