from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    personal_id = models.CharField(max_length=9)
    personal_doc = models.CharField(max_length=11, unique=True)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=11, default="")

    def __str__(self):
        return self.name


class Course(models.Model):
    LEVEL = (("B", "Basic"), ("I", "Intermediate"), ("A", "Advanced"))
    course_code = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    level = models.CharField(
        max_length=1, choices=LEVEL, blank=False, null=False, default="B"
    )

    def __str__(self):
        return self.description


class Matriculation(models.Model):
    PERIOD = (("M", "Morning"), ("A", "Afternoon"), ("N", "Night"))
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    period = models.CharField(
        max_length=1, choices=PERIOD, blank=False, null=False, default="M"
    )
