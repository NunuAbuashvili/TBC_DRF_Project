from rest_framework import serializers

from store.models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at')


class ProductSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    category_products = ProductSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'category_products', 'is_active']
