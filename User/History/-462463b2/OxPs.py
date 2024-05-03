from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EntityViewSet

router = DefaultRouter()
router.register('', EntityViewSet, basename='entity')

urlpatterns = [
    path('', include(router.urls)),
]
