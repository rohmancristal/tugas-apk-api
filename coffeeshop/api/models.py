from django.db import models

class Menu(models.Model):
    nama = models.CharField(max_length=255)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    status_tersedia = models.BooleanField(default=True)

class Kategori(models.Model):
    nama = models.CharField(max_length=255)

class Pesanan(models.Model):
    waktu_pemesanan = models.DateTimeField(auto_now_add=True)
    total_harga = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=(('Menunggu', 'Menunggu'), ('Diproses', 'Diproses'), ('Selesai', 'Selesai')))
    metode_pembayaran = models.CharField(max_length=20, choices=(('Tunai', 'Tunai'), ('Debit', 'Debit'), ('Kredit', 'Kredit')))
    meja = models.ForeignKey('Meja', on_delete=models.CASCADE, null=True, blank=True)
    pelanggan = models.ForeignKey('Pelanggan', on_delete=models.CASCADE, null=True, blank=True)

class Pelanggan(models.Model):
    nama = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=20)
    alamat = models.TextField()
    tanggal_bergabung = models.DateField(auto_now_add=True)

class Meja(models.Model):
    nomor_meja = models.IntegerField()
    kapasitas = models.IntegerField()
    status = models.CharField(max_length=20, choices=(('Tersedia', 'Tersedia'), ('Kosong', 'Kosong'), ('Dibersihkan', 'Dibersihkan')))





