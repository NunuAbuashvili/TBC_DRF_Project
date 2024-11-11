from rest_framework import serializers

from store.models import Product, Category


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.StringRelatedField()
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at')
        extra_kwargs = {
            'url': {'view_name': 'api:product-detail', 'lookup_field': 'pk'}
        }


class ProductSimpleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'url']
        extra_kwargs = {
            'url': {'view_name': 'api:product-detail', 'lookup_field': 'pk'}
        }


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    category_products = ProductSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'url', 'name', 'slug', 'description', 'category_products']
        extra_kwargs = {
            'url': {'view_name': 'api:category-detail', 'lookup_field': 'slug'}
        }
