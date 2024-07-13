from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AchievementViewSet

# router = DefaultRouter()
# router.register(r'achievements', AchievementViewSet)

router = DefaultRouter()
router.register('', AchievementViewSet, basename='achievements')

urlpatterns = [
    path('show/', AchievementViewSet.as_view({'get': 'list'}), name='entity-list'),
    path('create/', EntityViewSet.as_view({'post': 'create'}), name='entity-create'),
    path('<int:id>/update/', EntityViewSet.as_view({'put': 'update'}), name='entity-update'),
    path('<int:id>/delete/', EntityViewSet.as_view({'delete': 'destroy'}), name='entity-delete'),
]