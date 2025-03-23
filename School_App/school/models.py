from django.db import models
from django.contrib.auth.models import User

# Адреса на училиштето
class Address(models.Model):
    street = models.CharField(max_length=100)
    str_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.street} {self.str_number}"

# Училиште
class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    principal = models.CharField(max_length=255)
    employee_count = models.PositiveIntegerField(default=0)
    student_count = models.PositiveIntegerField(default=0)
    founded_date = models.DateField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Ученик
class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birth_date = models.DateField()
    grade = models.IntegerField()
    parent_number = models.CharField(max_length=100)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname} (Grade {self.grade}) - {self.school}"

# Наставник
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    ssn = models.CharField(max_length=100, unique=True)
    salary = models.IntegerField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname} - {self.school}"

# Предмет
class Subject(models.Model):
    name = models.CharField(max_length=100)
    grade = models.IntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="subjects")

    def __str__(self):
        return self.name

# Врска помеѓу наставник и предмет
class TeacherSubject(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject} - {self.teacher}"
