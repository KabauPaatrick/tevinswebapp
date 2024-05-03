from django.urls import path
from .views import EntityViewSet

urlpatterns = [
    path('show/', EntityViewSet.as_view({'get': 'list'}), name='entity-list'),
    path('create/', EntityViewSet.as_view({'post': 'create'}), name='entity-create'),
    path('<int:id>/update/', EntityViewSet.as_view({'put': 'update'}), name='entity-update'),
    path('<int:id>/delete/', EntityViewSet.as_view({'delete': 'destroy'}), name='entity-delete'),
]
