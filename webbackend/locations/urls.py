# locations/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet

router = DefaultRouter()
router.register(r'', LocationViewSet, basename='location')

urlpatterns = [
    path('list/', LocationViewSet.as_view({'get': 'list'}), name='location-list'),
    path('create/', LocationViewSet.as_view({'post': 'create'}), name='location-create'),
    path('<uuid:pk>/update/', LocationViewSet.as_view({'put': 'update'}), name='location-update'),
    path('<uuid:pk>/delete/', LocationViewSet.as_view({'delete': 'destroy'}), name='location-delete'),
]

urlpatterns += router.urls
