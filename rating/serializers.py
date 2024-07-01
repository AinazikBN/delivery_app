from rest_framework import serializers
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='onwer.email')
    menu = serializers.ReadOnlyField(source='menu.title')

    class Meta:
        model = Rating
        fields = '__all__'