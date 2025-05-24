from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Course(models.Model):
    TYPE_COURSES = [
        ("O", "Online"),
        ("P", "Physically")
    ]
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    type = models.CharField(max_length=1, choices=TYPE_COURSES)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f"{self.name} {self.type}"


class Lecturer(models.Model):
    LECTURER_TYPES = [
        ("P", "Professor"),
        ("A", "Assistant"),
        ("D", "Demonstrator")

    ]
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=1, choices=LECTURER_TYPES, null=True, blank=True)
    mail = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100,null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname} - {self.type}"


class CourseLecturer(models.Model):
    lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL,null=True, related_name='courses')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f"{self.lecturer.name} {self.course.name}"
