from rest_framework import viewsets
from .models import Entity
from .serializers import EntitySerializer

class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
    lookup_field = 'id' 
