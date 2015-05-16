from django.db import models
from django_extensions.db.models import TimeStampedModel


class Station(TimeStampedModel):
    name = models.TextField()
