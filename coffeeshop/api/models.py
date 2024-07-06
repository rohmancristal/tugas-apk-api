from django.db import models

class Menu(models.Model):
    nama = models.CharField(max_length=255)
    deskripsi = models.TextField()
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    kategori = models.ForeignKey('Kategori', on_delete=models.CASCADE)
    status_tersedia = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nama} ({self.harga})" 

class Kategori(models.Model):
    nama = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nama}"

class Pesanan(models.Model):
    waktu_pemesanan = models.DateTimeField(auto_now_add=True)
    total_harga = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=(('Menunggu', 'Menunggu'), ('Diproses', 'Diproses'), ('Selesai', 'Selesai')))
    metode_pembayaran = models.CharField(max_length=20, choices=(('Tunai', 'Tunai'), ('Debit', 'Debit'), ('qris', 'qris')))

    def __str__(self):
        return f"Pesanan #{self.id} dari {self.pelanggan.nama} ({self.status})"

class Pelanggan(models.Model):
    nama = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=20)
    alamat = models.TextField()
    email = models.EmailField(unique=True)
    tanggal_bergabung = models.DateField(auto_now_add=True)
    poin_loyalitas = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nama} ({self.nomor_telepon})"

class Meja(models.Model):
    nomor_meja = models.IntegerField()
    kapasitas = models.IntegerField()
    status = models.CharField(max_length=20, choices=(('Tersedia', 'Tersedia'), ('Kosong', 'Kosong'), ('Dibersihkan', 'Dibersihkan')))

    def __str__(self):
        return f"Meja #{self.nomor_meja} ({self.kapasitas} orang) ({self.status})"





