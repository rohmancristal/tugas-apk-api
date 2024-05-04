from django.contrib import admin
from .models import Menu, Kategori, Pesanan, Pelanggan, Meja

class tb_Menu(admin.ModelAdmin):
    list_display = ('nama','deskripsi','harga','kategori','status_tersedia')
    list_display_links = ('nama','deskripsi','harga','kategori','status_tersedia')
    search_fields = ('nama')
    list_per_page = 5

class tb_Kategori(admin.ModelAdmin):
    list_display = ('nama')
    list_display_links = ('nama')
    search_fields = ('nama')
    list_per_page = 5

class tb_Pesanan(admin.ModelAdmin):
    list_display = ('waktu_pemesanan','total_harga','status','metode_pembayaran','catatan', 'meja', 'pelanggan')
    list_display_links = ('waktu_pemesanan','total_harga','status','metode_pembayaran','catatan', 'meja', 'pelanggan')
    search_fields = ('total_harga')
    list_per_page = 5

    'admin.site.register(menu, tb_Menu)'
    'admin.site.register(menu, tb_Kategori)'
    'admin.site.register(menu, tb_Pesanan)'