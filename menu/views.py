from django.shortcuts import render
from .models import Menu
from .serializers import MenuSerializers
from rest_framework.viewsets import ModelViewSet
from .permissions import IsAuthororAdmin
from rest_framework.response import Response
from rest_framework.decorators import action 
from rest_framework import permissions
from rating.serializers import RatingSerializer
from favorite.models import Favorite
from favorite.serializers import FavoriteSerializer
from django.core.cache import cache
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from category.models import Category

class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    category = filters.ModelChoiceFilter(queryset=Category.objects.all() )

class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def perform_create(self, serializer):
        cache.delete('menu_list')
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return (IsAuthororAdmin(), )
        return (permissions.IsAuthenticatedOrReadOnly(), )
    
    def list(self, request, *args, **kwargs):
        cache_key = 'menu_list'
        cached_response = cache.get(cache_key)
        if cached_response:
            return cached_response
        
        response = super().list(request, *args, **kwargs)
        cache.set(cache_key, response, 60*15) #15 minutes
        return response
    
    @action(['GET', 'POST', 'DELETE'], detail=True)
    def ratings(self, request, pk):
        menu = self.get_object()
        user = request.user
        if request.method == 'GET':
            rating = menu.ratings.all()
            serializer = RatingSerializer(instance=rating, many=True)
            return Response(serializer.data, status=200)
        elif request.method == 'POST':
            if menu.ratings.filter(owner=user).exists():
                return Response('Вы уже поставили оценку на этот товар', status=400)
            serializer = RatingSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(owner=user, menu=menu)
            return Response(serializer.data, status=201)
        else:
            if not menu.ratings.filter(owner=user).exists():
                return Response('Ты не можешь удалить, потому что ты не оставлял рейтинг на этот товар', status=400)
            menu.ratings.get(owner=user)
            rating.delete()
            return Response('Успешно удалено', status=204)
        
    @action(['POST', 'DELETE', 'GET'], detail=True)
    def favorite(self, request, pk):
        menu = self.get_object()
        user = request.user
        if request.method == 'POST':
            if user.favorites.filter(menu=menu).exists():
                return Response('This position is already in favorite', status=200)
            Favorite.objects.create(owner=user, menu=menu)
            return Response('Added to the Favorite')
        elif request.method == 'DELETE':
            favorite = user.favorites.filter(menu=menu)
            if favorite.exists():
                favorite.delete()
                return Response('You delete position is favorite', status=204)
            return Response('Position is not found', status=404)
        else:
            favorites = user.favorites.all()
            if favorites.exists():
                serializer = FavoriteSerializer(instance=favorites, many=True)
                return Response(serializer.data, status=200)
            else:
                return Response('This position is not in favorite', status=400)
        

  
    
