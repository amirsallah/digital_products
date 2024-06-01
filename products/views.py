from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Product, Category, File
from .serializer import ProductSerializer, CategorySerializer, FileSerializer


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductDetailView(APIView):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryDetailView(APIView):
    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class FileListView(APIView):
    def get(self, request, product_id):
        files = File.objects.filter(product_id=product_id)
        serializer = FileSerializer(files, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class FileDetailView(APIView):
    def get(self, request, pk, product_id):
        file = File.objects.get(pk=pk, product_id=product_id)
        serializer = FileSerializer(file, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
