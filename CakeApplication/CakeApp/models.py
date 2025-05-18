from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# Секоја торта има име, цена, тежина, опис и слика.
#

class Cake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.IntegerField()
    weight = models.FloatField()
    description = models.TextField(max_length=400)
    image = models.ImageField(upload_to='cakes/', null=True, blank=True)
    baker = models.ForeignKey("Baker", on_delete=models.CASCADE, related_name='cakes')

    def __str__(self):
        return self.name + " " + str(self.price)


# Системот има и корисници (пекари) кои можат да додаваат
# нови торти. Секој од овие корисници има име, презиме,
# телефон за контакт и email адреса. Точно се знае кој пекар ја има
# додадено која торта. Само пекарот што ја има додадено тортата може
# да прави промени на истата.
#
class Baker(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,)
    image = models.ImageField(upload_to='bakers/', null=True, blank=True)
    def __str__(self):
        return self.name + " " + self.surname

# За да може подобро да ја демонстрирате апликацијата,
# треба да имате додадено барем два пекари и тортите кои
# се дефинирани на страната index.
