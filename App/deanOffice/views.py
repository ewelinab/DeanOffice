# TO DO
# 1 stworzenie 2 serwisów, ktore pozwala odczytac:-----------------DONE
# a. aktualnie obsługiwany i (nazwa: getActualNumber)-----------------DONE
# b. pierwszy dostępny numerek z bazy (nazwa: getAvailableNumber)-----------------DONE
# 2 implementacjia serwisów w aplikacji mobilnej: getActualNumber; getAvailableNumber
# 3 Logowanie studenta do ap mobilnej
# 4 Logowanie employee do serwisu deanOffice
# 5 REzerwacja numerka
# a. mobilna
# b. serwis rezerwujący (trivial - )

from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.shortcuts import render
from .models import Student
from .models import Employee
from .models import NumbersQueue
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login/')
def dean_office(request):
    print(request.user)
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

@login_required(login_url='/login/')
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

def dean_calculate_available_number():

    available_number = NumbersQueue.objects.last()

    if available_number is not None:
        num = available_number.numberId + 1
    else:
        num = 1

    return num

def dean_get_available_number(request):
    num = dean_calculate_available_number()
    return HttpResponse("{}".format(num))

def dean_reserve_number(request, login):
    num = dean_calculate_available_number()
    #TODO: syie sie jak student poda login, ktorego nie ma w bazie studentow
    student = Student.objects.get(studentId = login)
    NumbersQueue.objects.create(numberId = num, studentId = student)
    return HttpResponse("{}".format(num))

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def welfare_next_number(request):
    NumbersQueue.objects.first().delete()
    return welfare_office(request)
