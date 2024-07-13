from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    path('show/', CustomerViewSet.as_view({'get': 'list'}), name='solution-list'),
    path('create/', CustomerViewSet.as_view({'post': 'create'}), name='solution-create'),
    path('<uuid:pk>/update/', CustomerViewSet.as_view({'put': 'update'}), name='solution-update'),
    path('<uuid:pk>/delete/', CustomerViewSet.as_view({'delete': 'destroy'}), name='solution-delete'),
]
