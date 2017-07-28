from django.db import models

class Employee(models.Model):
    employeeId = models.CharField(primary_key=True, max_length=20)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)

    def __str__(self):
        return 'Id={}, Imie={}, Nazwisko={}'.format(self.employeeId, self.firstName, self.lastName)


class Student(models.Model):
    studentId = models.CharField(primary_key=True, max_length=20)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    faculty = models.CharField(max_length=100)
    groupId = models.CharField(max_length=50)

    def __str__(self):
        return self.studentId


class NumbersQueue(models.Model):
    numberId = models.IntegerField(primary_key=True)
    studentId = models.ForeignKey('Student')

    def __str__(self):
        return str(self.numberId)
