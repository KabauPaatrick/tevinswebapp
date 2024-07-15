from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EntityViewSet

router = DefaultRouter()
router.register('', EntityViewSet, basename='entity')

urlpatterns = [
    path('show/', EntityViewSet.as_view({'get': 'list'}), name='solution-list'),
    path('create/', EntityViewSet.as_view({'post': 'create'}), name='solution-create'),
    path('<uuid:pk>/update/', EntityViewSet.as_view({'put': 'update'}), name='solution-update'),
    path('<uuid:pk>/delete/', EntityViewSet.as_view({'delete': 'destroy'}), name='solution-delete'),
]

