from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HomeViewViewSet

router = DefaultRouter()
router.register('', HomeViewViewSet, basename="homeview")

urlpatterns = [
    path('', include(router.urls)),
]
