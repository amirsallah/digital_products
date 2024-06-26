from rest_framework import serializers

from .models import Product, Category, File


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('url', 'id', 'title', 'description', 'avatar')


class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'title', 'file')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(many=True)
    files = FileSerializer(many=True)

    class Meta:
        model = Product
        fields = ('url', 'id', 'title', 'description', 'avatar', 'category', 'files')
