from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Band(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date = models.DateTimeField()
    events_attended = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.country}-{self.events_attended}"


class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    image = models.ImageField(blank=True, null=True, upload_to="event_photos/")
    is_outside = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.date}-{self.is_outside}"


class BandEvent(models.Model):
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.band.name} {self.event.name}"
