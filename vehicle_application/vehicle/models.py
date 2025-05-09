from django.db import models
from django.contrib.auth.models import User


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    year_of_establishment = models.CharField(max_length=5)
    num_employees = models.IntegerField()

    def __str__(self):
        return f"{self.name}"



class Car(models.Model):
    TYPE_CAR = [
        ("S", "Sedan"),
        ("SV", "SUV"),
        ("H", "Hatchback"),
        ("C", "Coupe")
    ]
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(decimal_places=2,max_digits=4)
    chassis_number = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=100)
    year_of_production = models.CharField(max_length=5)
    mileage = models.CharField(max_length=10)
    type = models.CharField(max_length=2, choices=TYPE_CAR)
    photo = models.ImageField(upload_to="car_photos/", null=True, blank=True)

    def __str__(self):
        return f"{self.manufacturer.name} {self.type}-{self.price}"
