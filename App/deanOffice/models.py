from django.db import models
from django.contrib.auth import models as auth_models

class Student(models.Model):
    studentId = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=200)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    faculty = models.CharField(max_length=100)
    groupId = models.CharField(max_length=50)

    def __str__(self):
        return self.studentId

class DeanOfficeNumbersQueue(models.Model):
    numberId = models.IntegerField(primary_key=True)
    studentId = models.ForeignKey('Student')

    def __str__(self):
        return str(self.numberId)

class WelfareOfficeNumbersQueue(models.Model):
    numberId = models.IntegerField(primary_key=True)
    studentId = models.ForeignKey('Student')

    def __str__(self):
        return str(self.numberId)
