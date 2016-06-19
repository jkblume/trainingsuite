from django.db import models
from django.utils import timezone


# Create your models here.
class Training(models.Model):
    athlete = models.CharField(max_length=200)
    distance = models.FloatField()
    current_distance = models.FloatField()
    gpx_file_path = models.CharField(max_length=200)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
