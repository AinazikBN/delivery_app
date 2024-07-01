from django.shortcuts import render
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Comment
from rest_framework import generics, permissions
from menu.permissions import IsAuthor
from .serializers import CommentSerializer
from rest_framework.decorators import action 
from rest_framework.response import Response
from favorite.models import Like
from favorite.serializers import LikeSerializer
from rest_framework.viewsets import ModelViewSet

class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


    
    @action(methods=['POST', 'DELETE'], detail=True)
    def like(self, request, pk=None):
        comment = self.get_object()
        user = request.user
        if request.method == 'POST':
            if user.likes.filter(comment=comment).exists():
                return Response('This comment has already liked', status=201)
            Like.objects.create(owner=user, comment=comment)
            return Response('You liked this comment', status=201)
        elif request.method == 'DELETE':
            like = user.likes.filter(owner=user, comment=comment).first()
            if like:
                like.delete()
                return Response('Like has been removed', status=204)
            return Response('You have not liked this comment', status=404)
        # else:
        #     likes = comment.likes.all()
        #     serializer = LikeSerializer(instance=likes, many=True)
        #     return Response(serializer.data, status=200)
        
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['likes'] = LikeSerializer(instance.likes.all(), many=True).data
    #     representation['quantity of likes'] = 0
    #     for _ in representation['likes']:
    #         representation['quantity of likes'] += 1
