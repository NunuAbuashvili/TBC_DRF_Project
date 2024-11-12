from django.shortcuts import render

from rest_framework.generics import ListAPIView, ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from store.models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class ProductListView(ListCreateAPIView):
    queryset = Product.objects.select_related('category').prefetch_related('tags')
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.select_related('category').prefetch_related('tags')
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CategoryListView(ListCreateAPIView):
    queryset = Category.objects.prefetch_related('category_products')
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CategoryDetailView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_slug = self.kwargs.get('slug')
        queryset = Product.objects.filter(
            category__slug=category_slug
        ).select_related('category').prefetch_related('tags')
        return queryset
