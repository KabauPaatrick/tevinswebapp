# locations/serializers.py
from rest_framework import serializers
from .models import Location

class LocationSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Location
        fields = ('id', 'name', 'description', 'parent', 'children')

    def get_children(self, obj):
        serializer = LocationSerializer(obj.get_children(), many=True)
        return serializer.data
