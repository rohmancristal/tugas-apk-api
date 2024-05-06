from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuViewSet, KategoriViewSet, PesananViewSet, PelangganViewSet, MejaViewSet

router = DefaultRouter()
router.register(r'Menu', MenuViewSet)
router.register(r'Kategori', KategoriViewSet)
router.register(r'Pesanan', PesananViewSet)
router.register(r'Pelanggan', PelangganViewSet)
router.register(r'Meja', MejaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
