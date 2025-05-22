from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Travel(models.Model):
    place_name = models.CharField(max_length=100, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to="travel_photos/", null=True, blank=True)
    guide = models.ForeignKey('Guide', on_delete=models.CASCADE, null=True, blank=True, related_name='travel')

    def __str__(self):
        return self.place_name

class Guide(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name + " " +self.surname