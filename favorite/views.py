from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from .models import Like
from .serializers import LikeSerializer, FavoriteSerializer
from menu.models import Menu
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model() 

class LikeCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LikeSerializer 

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
