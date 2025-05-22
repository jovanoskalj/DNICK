from django.db import models
from django.contrib.auth.models import  User


class Travel (models.Model):
    destination = models.CharField(max_length=100)
    price = models.IntegerField()
    duration = models.IntegerField()
    image = models.ImageField()
    guide = models.ForeignKey("Guide", on_delete=models.CASCADE, related_name='travel')

    def __str__(self):
        return f"{self.destination} {self.duration}"

class Guide (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.surname}"



