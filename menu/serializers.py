from rest_framework import serializers
from .models import Menu, MenuImages
from category.models import Category
from favorite.serializers import FavoriteSerializer
from django.db.models import Avg

class MenuImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuImages
        fields = '__all__'

class MenuSerializers(serializers.ModelSerializer):
    owner_email = serializers.ReadOnlyField(source='owner.email')
    owner = serializers.ReadOnlyField(source='owner.id')
    images = MenuImagesSerializer(many=True, required=False)

    class Meta:
        model = Menu
        fields = '__all__'
        images = MenuImagesSerializer(many=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['favorites'] = FavoriteSerializer(instance.favorites.all(), many=True).data
        representation['quantity of favorites'] = 0
        for _ in representation['favorites']:
            representation['quantity of favorites'] += 1
        representation['rating'] = instance.ratings.aggregate(
            Avg('rating')
        )
        representation['rating_count'] = instance.ratings.count()
        return representation
    

