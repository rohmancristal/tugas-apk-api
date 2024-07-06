from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Menu, Kategori, Pesanan, Pelanggan, Meja
from .serializers import MenuSerializer, KategoriSerializer, PesananSerializer, PelangganSerializer, MejaSerializer


class MenuListCreateAPIView(APIView):
    def get(self, request):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MenuDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Menu, pk=pk)

    def get(self, request, pk):
        menu = self.get_object(pk)
        serializer = MenuSerializer(menu)
        return Response(serializer.data)

    def put(self, request, pk):
        menu = self.get_object(pk)
        serializer = MenuSerializer(menu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        menu = self.get_object(pk)
        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class KategoriListCreateAPIView(APIView):
    def get(self, request):
        kategoris = Kategori.objects.all()
        serializer = KategoriSerializer(kategoris, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = KategoriSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KategoriDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Kategori, pk=pk)

    def get(self, request, pk):
        kategori = self.get_object(pk)
        serializer = KategoriSerializer(kategori)
        return Response(serializer.data)

    def put(self, request, pk):
        kategori = self.get_object(pk)
        serializer = KategoriSerializer(kategori, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        kategori = self.get_object(pk)
        kategori.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PesananListCreateAPIView(APIView):
    def get(self, request):
        pesanans = Pesanan.objects.all()
        serializer = PesananSerializer(pesanans, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PesananSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PesananDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Pesanan, pk=pk)

    def get(self, request, pk):
        pesanan = self.get_object(pk)
        serializer = PesananSerializer(pesanan)
        return Response(serializer.data)

    def put(self, request, pk):
        pesanan = self.get_object(pk)
        serializer = PesananSerializer(pesanan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pesanan = self.get_object(pk)
        pesanan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PelangganListCreateAPIView(APIView):
    def get(self, request):
        pelanggans = Pelanggan.objects.all()
        serializer = PelangganSerializer(pelanggans, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PelangganSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PelangganDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Pelanggan, pk=pk)

    def get(self, request, pk):
        pelanggan = self.get_object(pk)
        serializer = PelangganSerializer(pelanggan)
        return Response(serializer.data)

    def put(self, request, pk):
        pelanggan = self.get_object(pk)
        serializer = PelangganSerializer(pelanggan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pelanggan = self.get_object(pk)
        pelanggan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MejaListCreateAPIView(APIView):
    def get(self, request):
        mejas = Meja.objects.all()
        serializer = MejaSerializer(mejas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MejaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MejaDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Meja, pk=pk)

    def get(self, request, pk):
        meja = self.get_object(pk)
        serializer = MejaSerializer(meja)
        return Response(serializer.data)

    def put(self, request, pk):
        meja = self.get_object(pk)
        serializer = MejaSerializer(meja, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        meja = self.get_object(pk)
        meja.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
