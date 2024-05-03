from django.db import models
from django.db import models

class Testimonial(models.Model):
    author = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.author


# Create your models here.
