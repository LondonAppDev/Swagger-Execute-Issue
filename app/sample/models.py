from django.db import models

# Create your models here.

class SampleModel(models.Model):
    """Sample model."""
    description = models.TextField()
