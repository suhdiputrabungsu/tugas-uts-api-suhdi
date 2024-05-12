from django.db import models

class Penulis(models.Model):
    nama = models.CharField(max_length=255)

class Kategori(models.Model):
    nama = models.CharField(max_length=255)

class Buku(models.Model):
    judul = models.CharField(max_length=255)
    penulis = models.ForeignKey(Penulis, on_delete=models.CASCADE)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    stok = models.IntegerField()
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='buku/')
