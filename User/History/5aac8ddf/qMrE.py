from django.urls import path
from .views import TestimonialViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', TestimonialViewSet, basename='testimonial')

urlpatterns = [
    path('testimonials/', TestimonialViewSet.as_view({'get': 'list', 'post': 'create'}), name='testimonial-list-create'),
    path('testimonials/<uuid:pk>/', TestimonialViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='testimonial-retrieve-update-destroy'),
]
