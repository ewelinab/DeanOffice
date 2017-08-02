# TO DO
# 1 stworzenie 2 serwisów, ktore pozwala odczytac:
# a. aktualnie obsługiwany i (nazwa: getActualNumber)
# b. pierwszy dostępny numerek z bazy (nazwa: getAvailableNumber)
# 2 implementacjia serwisów w aplikacji mobilnej: getActualNumber; getAvailableNumber
# 3 Logowanie studenta do ap mobilnej
# 4 Logowanie employee do serwisu deanOffice
# 5 REzerwacja numerka
# a. mobilna
# b. serwis rezerwujący (trivial - )


from django.shortcuts import render
from .models import Student
from .models import Employee
from .models import NumbersQueue
# Create your views here.
def dean_office(request):
# nie dziala dla koncowki ze sleszem
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


def dean_next_number(request):

    num = NumbersQueue.objects.first()

    if num is not None:
        num.delete()

    return dean_office(request)

def dean_get_actual_number(request):

    actual_number = NumbersQueue.objects.first()

    if actual_number is not None:
        num = actual_number.numberId
    else:
        num = 0

    return render(request, 'dean_office/1.html', {'num': num})

def dean_get_available_number(request):

    available_number = NumbersQueue.objects.last()

    if available_number is not None:
        num = available_number.numberId + 1
    else:
        num = 1

    return render(request, 'dean_office/1.html', {'num': num})


def welfare_office(request):
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


    return render(request, 'dean_office/main.html', {'num': num, 'student': student, 'current_user': current_user, 'nextNumberLink': 'welfareOffice/nextNumber'})


def welfare_next_number(request):
    NumbersQueue.objects.first().delete()
    return welfare_office(request)
