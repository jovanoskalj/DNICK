from attr.validators import max_len
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Секоја
# хотелска резервација се карактеризира со код на резервацијата,
# почетен и краен датум на резервацијата, соба која се резервира,
# корисник кој ја направил резервацијата, слика од лична карта,
# информација дали е потврдена резервацијата
# и вработен во хотелот -рецепционер кој ја потврдил резервацијата.
class Reservation(models.Model):
    code = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE, null=True, blank=True)
    guest = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ID_photo = models.ImageField(upload_to='images/', null=True, blank=True)
    isConfirmed = models.BooleanField(default=False)
    receptionist = models.ForeignKey("Employee", on_delete=models.CASCADE, null=True, blank=True,
                                     limit_choices_to={'type': 'R'})

    def __str__(self):
        return f"{self.code} - {self.room}"


# За секој вработен во хотелот се чуваат неговото име и презиме,
# опис на работните задачи, година на вработување
# и тип на вработен (хигиеничар, рецепционер или менаџер).
class Employee(models.Model):
    TYPE_EMPLOYEE = [
        ("H", "Hygienist"),
        ("R", "Receptionist"),
        ("M", "Manager"),
    ]
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    date_started = models.DateField()
    type = models.CharField(max_length=1, choices=TYPE_EMPLOYEE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.surname}"


# Секоја соба е опишана преку нејзиниот број,
# број на кревети, информација дали собата располага со тераса и
# статус дали собата во моментот е исчистена. Дополнително,
# за секоја соба се доделуваат вработени во хотелот – хигиеничари
# кои треба да ја исчистат.
# На една соба може да бидат доделени повеќе хигиеничари

class Room(models.Model):
    room_number = models.IntegerField()
    bed_number = models.IntegerField()
    hasTerrace = models.BooleanField(default=True)
    isCleaned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.room_number} - {self.isCleaned}"


class RoomHygienist(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, limit_choices_to={'type': 'H'})
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.employee.name} - {self.room.room_number}"
