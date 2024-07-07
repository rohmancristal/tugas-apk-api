from django.urls import path
from .views import (
    MenuListCreateAPIView, MenuDetailAPIView,
    PesananListCreateAPIView, PesananDetailAPIView,
    PelangganListCreateAPIView, PelangganDetailAPIView,
    MejaListCreateAPIView, MejaDetailAPIView
)

urlpatterns = [
    path('menu/', MenuListCreateAPIView.as_view(), name='menu-list-create'),
    path('menu/<int:pk>/', MenuDetailAPIView.as_view(), name='menu-detail'),
    
    path('pesanan/', PesananListCreateAPIView.as_view(), name='pesanan-list-create'),
    path('pesanan/<int:pk>/', PesananDetailAPIView.as_view(), name='pesanan-detail'),
    
    path('pelanggan/', PelangganListCreateAPIView.as_view(), name='pelanggan-list-create'),
    path('pelanggan/<int:pk>/', PelangganDetailAPIView.as_view(), name='pelanggan-detail'),
    
    path('meja/', MejaListCreateAPIView.as_view(), name='meja-list-create'),
    path('meja/<int:pk>/', MejaDetailAPIView.as_view(), name='meja-detail'),
]
