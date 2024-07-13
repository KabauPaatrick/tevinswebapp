from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HomeViewViewSet

router = DefaultRouter()
router.register('', HomeViewViewSet, basename="homeview")

urlpatterns = [
    path('show/', AchievementViewSet.as_view({'get': 'list'}), name='achievement-list'),
    path('create/', AchievementViewSet.as_view({'post': 'create'}), name='achievement-create'),
    path('<int:id>/update/', AchievementViewSet.as_view({'put': 'update'}), name='achievement-update'),
    path('<int:id>/delete/', AchievementViewSet.as_view({'delete': 'destroy'}), name='achievement-delete'),
]
