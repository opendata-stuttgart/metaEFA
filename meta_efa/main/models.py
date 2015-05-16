from django.db import models
from django_extensions.db.models import TimeStampedModel


class Station(TimeStampedModel):
    station_id = models.TextField(primary_key=True)
    name = models.TextField()
    full_name = models.TextField()
