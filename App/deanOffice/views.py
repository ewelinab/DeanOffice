from django.shortcuts import render
from .models import Student
from .models import Employee
from .models import NumbersQueue
# Create your views here.
def main_site(request):
    current_user = Employee.objects.first()

    num = NumbersQueue.objects.first()

    if num is None:
        num = NumbersQueue()
        num.numberId = 0
        student = Student()
        student.studentId = "---"
        student.firstName = "---"
        student.lastName = ""
        student.faculty = "---"
        student.groupId = "---"
    else:
        student = num.studentId


    return render(request, 'dean_office/main.html', {'num': num, 'student': student, 'current_user': current_user})
