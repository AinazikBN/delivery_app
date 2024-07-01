from rest_framework import serializers
from .models import Like, Favorite
from rest_framework.response import Response
from django.contrib.auth import get_user_model
User = get_user_model() 

class LikeSerializer(serializers.ModelSerializer):
    owner_id = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Like
        fields = '__all__'

    def validate(self, attrs):
        request = self.context.get('request')
        user = request.user
        comment = attrs['comment']
        if user.likes.filter(comment=comment).exists():
            raise serializers.ValidationError(
                'You have already liked this comment!'
            )
        return attrs
    
class FavoriteSerializer(serializers.ModelSerializer):
    owner_email = serializers.ReadOnlyField(source='onwer.email')

    class Meta:
        model = Favorite
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['menu_title'] = instance.menu.title
        return representation