from django.db import models
from django.utils import timezone
from entity.models import Entity

class HomeView(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    ctatext = models.CharField(max_length=255)

    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to='media/homeview_images/')
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)  # Set default to current time
    updated_at = models.DateTimeField(default=timezone.now)  # Set default to current time

    def __str__(self):
        return self.title
