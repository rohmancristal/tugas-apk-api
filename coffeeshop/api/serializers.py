from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Menu, Kategori, Pesanan, Pelanggan, Meja

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'

class PesananSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesanan
        fields = '__all__'

class PelangganSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=Pelanggan.objects.all(), message="Pelanggan dengan email ini sudah ada.")]
    )

    class Meta:
        model = Pelanggan
        fields = '__all__'

class MejaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meja
        fields = '__all__'
