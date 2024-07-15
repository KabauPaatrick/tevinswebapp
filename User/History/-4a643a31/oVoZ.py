from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HomeViewViewSet

router = DefaultRouter()
router.register('', HomeViewViewSet, basename="homeview")

urlpatterns = [
    path('show/', HomeViewViewSet.as_view({'get': 'list'}), name='achievement-list'),
    path('create/', HomeViewViewSet.as_view({'post': 'create'}), name='achievement-create'),
    path('<int:id>/update/', HomeViewViewSet.as_view({'put': 'update'}), name='achievement-update'),
    path('<int:id>/delete/', HomeViewViewSet.as_view({'delete': 'destroy'}), name='achievement-delete'),
]
