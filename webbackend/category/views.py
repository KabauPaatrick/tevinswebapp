# views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer
# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            "success": True,
            "data": serializer.data,
            "message": "Product category created successfully"
        }, status=status.HTTP_201_CREATED, headers=headers)


