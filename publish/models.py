from django.db import models
from django.utils import timezone


# Create your models here.
class Training(models.Model):
    athlete = models.CharField(max_length=200)
    distance = models.FloatField(default=0)
    current_distance = models.FloatField(default=0)
    current_long = models.FloatField(default=0)
    current_lang = models.FloatField(default=0)
    current_alt = models.FloatField(default=0)
    gpx_file_path = models.CharField(max_length=200)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
