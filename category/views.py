from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer
from category.models import Category
from rest_framework import permissions

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'create', 'destroy']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]
