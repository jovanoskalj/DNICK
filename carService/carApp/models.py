from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Service (models.Model):
    code = models.CharField(max_length=50)
    date = models.DateField()
    description = models.TextField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="images/")
    car = models.ForeignKey("Car", on_delete=models.CASCADE)
    service_place = models.ForeignKey("ServicePlace", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code} {self.service_place.name}"

class Car (models.Model):
    CAR_TYPES = [
        ("A","Dzip"),
        ("B","SUV"),
        ("C","Sedan")
    ]
    type = models.CharField(max_length=1,choices=CAR_TYPES)
    manufacturer = models.ForeignKey("Manufacturer", on_delete=models.CASCADE)
    max_speed = models.IntegerField()
    color = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.type} {self.manufacturer.name}"

class ServicePlace(models.Model):
    name = models.CharField(max_length=100)
    year = models.DateField()
    idOldTimerService = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} {self.idOldTimerService}"


class Manufacturer (models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    origin = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.owner}"


class ServicePlaceManufacturer (models.Model):
    servicePlace = models.ForeignKey(ServicePlace, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.servicePlace.name} {self.manufacturer.name}"