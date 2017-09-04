import names
from django.http import HttpResponse

from .models import Student, DeanOfficeNumbersQueue, WelfareOfficeNumbersQueue
from .views import *
import hashlib

def fill_database(request):
    generateStudents(50)
    # clearTable(DeanOfficeNumbersQueue)
    # clearTable(DeanOfficStudenteNumbersQueue)
    return HttpResponse("Done.")

def clear_database(request):
    clearTable(DeanOfficeNumbersQueue)
    clearTable(WelfareOfficeNumbersQueue)
    clearTable(Student)
    return HttpResponse("Done.")

def clearTable(ModelName):
    for num in ModelName.objects.all():
        num.delete()

def generateStudents(nr_of_students):
    faculty_group = ['Informatyka', 'Fizyka', 'Matematyka']
    for i in range(1, nr_of_students):
        Student.objects.create(studentId=i,
                               password=hashlib.sha256('password'.encode('utf-8')).hexdigest(),
                               firstName=names.get_first_name(),
                               lastName=names.get_last_name(),
                               faculty=faculty_group[i%3],
                               groupId=i%10)



#test
def dean_reserve_number(request, login):
    return reserve_number(request, login, DeanOfficeNumbersQueue)

def welfare_reserve_number(request, login):
    return reserve_number(request, login, WelfareOfficeNumbersQueue)