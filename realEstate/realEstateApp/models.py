from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class RealEstate(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    area = models.FloatField()
    date = models.DateField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    isBooked = models.BooleanField(default=False)
    isSold = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.area}"


class Agent(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=100)
    linkedin_url = models.URLField()
    num_sells = models.IntegerField()
    mail = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.surname}"


class RealEstateAgent(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.agent.name} {self.agent.surname} - {self.real_estate.name}"


class Characteristics(models.Model):
    price = models.IntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.price}"


class RealEstateCharacteristics(models.Model):
    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE)
    characteristic = models.ForeignKey(Characteristics, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.real_estate.name} - {self.characteristic}"
