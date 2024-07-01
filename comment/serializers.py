from rest_framework import serializers
from .models import Comment
from favorite.serializers import LikeSerializer

class CommentSerializer(serializers.ModelSerializer):
    owner_email = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Comment
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['likes'] = LikeSerializer(instance.likes.all(), many=True).data
        representation['quantity of likes'] = 0
        for _ in representation['likes']:
            representation['quantity of likes'] += 1

    
        representation['menu_title'] = instance.menu.title
        if instance.menu.preview:
            preview = instance.menu.preview.url
            representation['menu_preview'] = preview
        return representation 
    