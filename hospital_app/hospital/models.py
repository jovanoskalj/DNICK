from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# Секоја болница се карактеризира со име, адреса (улица и број), телефонски број,
# емаил адреса, директор, број на лекари, број на пациенти, датум на основање и
# корисник кој ја додал болницата. Додавање и бришење на болници е дозволено само
# за супер корисници.
class Address(models.Model):
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street} {self.number}"


class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    principal = models.CharField(max_length=100)
    doctor_no = models.IntegerField()
    patient_no = models.IntegerField()
    date_formed = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name} {self.address}"


#  За секој лекар се чува неговото име, презиме, ЕМБГ,
#  специјализација, плата и корисник кој го додал. Еден лекар може да работи само
# во една болница. Откако лекарот ќе биде зачуван,
# истиот може да се промени и избрише само од корисникот кој го креирал.

class Doctor(models.Model):
    SPECIALIZATION_TYPES = [
        ("G", "General Medicine"),
        ("F", "Family Medicine"),
        ("I", "Internal Medicine"),

    ]
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    ssn = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100, choices=SPECIALIZATION_TYPES)
    salary = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name} {self.surname} {self.specialization} works at {self.hospital}"

    # Секоја болница има пациенти. За секој пациент се чува неговото име, презиме, датум на раѓање,
    #  матичен број, телефонски број за контакт, дијагноза и корисник кој го додал.
    #  Пациентите припаѓаат на една болница. Може да се менуваат и бришат само од
    #  корисникот кој ги додал.

class Patient(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birth_date = models.DateField()
    ssn = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    diagnosis = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname}"


# ANTIBIOTIC = "Antibiotic"
#     ANALGESIC = "Analgesic"
#     VITAMIN = "Vitamin"
#     ANTISEPTIC = "Antiseptic"
#     ANTIHISTAMINE = "Antihistamine"
# Во болницата се складираат лекови. За секој лек се чува неговото име,
# тип (антибиотик, аналгетик, витамин, антисептик, антихистаминик),
# дали е на рецепт, код и количина достапна во болницата. Лековите се
#  додаваат во делот за болници. Лековите може да се филтрираат според типот и дали се на рецепт.


class Drugs(models.Model):
    DRUG_TYPES = [
        ("antibiotic", "antibiotic"),
        ("antiseptic", "antiseptic"),
        ("analgesic", "analgesic"),
        ("vitamin", "vitamin"),
        ("antihistamine", "antihistamine"),
    ]
    name = models.CharField(max_length=100)
    prescription_required = models.BooleanField(default=False)
    drug_type = models.CharField(max_length=100, choices=DRUG_TYPES)
    code = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name} Prescription: {self.prescription_required} Code: {self.code}"


class HospitalDrugs(models.Model):
    drug = models.ForeignKey(Drugs, on_delete=models.SET_NULL, null=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.drug} Hospital: {self.hospital} Quantity: {self.quantity}"
