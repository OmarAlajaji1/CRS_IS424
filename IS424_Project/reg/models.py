from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class College(models.Model):
    collegeid = models.IntegerField()
    name = models.CharField(max_length=70)

    def str(self):
        return f"{self.collegeid} ({self.name})"


class Course(models.Model):
    name =  models.CharField(max_length=70)
    instructor=models.CharField(max_length=70)
    courseid = models.CharField(max_length=30)
    hours = models.IntegerField()
    hostcollege = models.ForeignKey(College, on_delete=models.CASCADE, related_name="courses")
    dicription=models.CharField(max_length=300)


    def str(self):
        return f"course info are name: {self.name} ,id: {self.courseid} , credit Hours: {self.hours} ,Host college : {self.hostcollege}"


class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # firstName = models.CharField(max_length=64)
    # lastName = models.CharField(max_length=64)
    #studentid = models.IntegerField(blank=True)
    courses = models.ManyToManyField(Course, blank=True, related_name="students")

    def str(self):
        return f"student info are name :{self.firstName} {self.lastName}"


