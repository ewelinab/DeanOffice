import names
from django.http import HttpResponse

from .models import Student
from .models import Employee
from .models import NumbersQueue

def fill_database(request):
    generate1Employee()
    generateStudents(500)
    return HttpResponse("Done.")


def generate1Employee():
    Employee.objects.create(employeeId=1, firstName='Elwirka', lastName='Kotowska')

def generateStudents(nr_of_students):
    faculty_group = ['Informatyka', 'Fizyka', 'Matematyka']
    for i in range(nr_of_students):
        Student.objects.create(studentId=i,
                               firstName=names.get_first_name(),
                               lastName=names.get_last_name(),
                               faculty=faculty_group[i%3],
                               groupId=i%10)
