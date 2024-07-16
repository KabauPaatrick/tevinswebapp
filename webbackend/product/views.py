from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Product
from .serializers import ProductSerializer, SingleProductResponseSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Override the retrieve method directly in ModelViewSet
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # Define a custom action for detailed response
    @action(detail=True, methods=['get'])
    def detailed_response(self, request, pk=None):
        product = self.get_object()
        serializer = ProductSerializer(product)
        response_data = {
            'success': True,
            'data': serializer.data,
            'message': 'Product retrieved successfully'
        }
        response_serializer = SingleProductResponseSerializer(response_data)
        return Response(response_serializer.data)
