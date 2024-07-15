from rest_framework import serializers
from .models import HomeView

class HomeViewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = HomeView
        fields = ['id', 'title', 'description', 'ctatext', 'entity', 'image']
