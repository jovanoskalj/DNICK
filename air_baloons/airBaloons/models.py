from django.db import models
from django.contrib.auth.models import User


#  За секој
# пилот се чуваат негово име и презиме, година на раѓање, вкупно часови налет и чин кој го
# има во компанијата. За секој балон се чуваат типот на балонот, име на производителот на
# балонот и максимален дозволен број на патници во балонот.

# Create your models here.

class Pilot(models.Model):
    POSITION_CHOICES = [
        ("JN", "Junior"),
        ("SN", "Senior"),
        ("IM", "Intermediate"),
    ]

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    total_flight_hours = models.IntegerField()
    position = models.CharField(max_length=2, choices=POSITION_CHOICES)

    def __str__(self):
        return self.name + " " + self.surname


# За секој балон се чуваат типот на балонот, име на производителот на
#  балонот и максимален дозволен број на патници во балонот.

class AirBalloon(models.Model):
    TYPE_CHOICES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    manufacturer = models.CharField(max_length=100)
    max_capacity = models.IntegerField()

    def __str__(self):
        return self.name


#  За авиокомпанијата се чува
# нејзиното име, година на основање и информација дали лета надвор од Европа или не.

class Airline(models.Model):
    name = models.CharField(max_length=100)
    year_founded = models.DateField()
    fliesOutsideEurope = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class PilotAirline(models.Model):
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)

    def __str__(self):
        return self.pilot.name + " " + self.airline.name


# Секој лет се карактеризира со задолжителна шифра, име на кој аеродром полетува и на кој
# аеродром слетува, корисник кој го креирал летот, фотографија за летот, информација со кој
# балон се изведува летот, пилот на летот и авиокомпанија која го реализира летот.
class Flight(models.Model):
    flightCode = models.CharField(max_length=100, blank=False, null=False)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    departureAirport = models.CharField(max_length=100, blank=False, null=False)
    arrivalAirport = models.CharField(max_length=100, blank=False, null=False)
    flightPhoto = models.ImageField(upload_to="flightPhotos")
    airBalloon = models.ForeignKey(AirBalloon, on_delete=models.CASCADE)
    flightPilot = models.ForeignKey(PilotAirline, on_delete=models.CASCADE)

    def __str__(self):
        return self.flightCode
