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
from .models import Student, DeanOfficeNumbersQueue, WelfareOfficeNumbersQueue
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import hashlib
# Create your views here.


def create_empty_student():
    student = Student()
    student.studentId = "---"
    student.firstName = "---"
    student.lastName = ""
    student.faculty = "---"
    student.groupId = "---"
    return student

def render_main_site(request, NumerQueueModel, next_number_view):
    num = NumerQueueModel.objects.first()
    if num is None:
        num = NumerQueueModel()
        num.numberId = 0
        student = create_empty_student()
    else:
        student = num.studentId
    return render(request, 'dean_office/main.html', {'num': num, 'student': student, 'next_number_view': next_number_view})

@login_required(login_url='/login/')
def dean_office(request):
    return render_main_site(request, DeanOfficeNumbersQueue, 'dean_next_number')

@login_required(login_url='/login/')
def dean_next_number(request):
    num = DeanOfficeNumbersQueue.objects.first()
    if num is not None:
        num.delete()
    return HttpResponseRedirect('/deanOffice/')

def get_actual_number(NumbersQueueModel):
    actual_number = NumbersQueueModel.objects.first()
    if actual_number is not None:
        num = actual_number.numberId
    else:
        num = 0
    return num

def dean_get_actual_number(request):
    return HttpResponse("{}".format(get_actual_number(DeanOfficeNumbersQueue)))

def calculate_available_number(NumbersQueueModel):
    available_number = NumbersQueueModel.objects.last()
    if available_number is not None:
        num = available_number.numberId + 1
    else:
        num = 1
    return num

def dean_get_available_number(request):
    return HttpResponse("{}".format(calculate_available_number(DeanOfficeNumbersQueue)))

def reserve_number(request, login, NumbersQueueModel):
    num = calculate_available_number(NumbersQueueModel)
    #TODO: syie sie jak student poda login, ktorego nie ma w bazie studentow
    student = Student.objects.get(studentId = login)
    NumbersQueueModel.objects.create(numberId = num, studentId = student)
    return HttpResponse("{}".format(num))

def dean_reserve_number(request, login):
    return reserve_number(request, login, DeanOfficeNumbersQueue)

#welfare

@login_required(login_url='/login/')
def welfare_office(request):
    return render_main_site(request, WelfareOfficeNumbersQueue, 'welfare_next_number')

@login_required(login_url='/login/')
def welfare_next_number(request):
    num = WelfareOfficeNumbersQueue.objects.first()
    if num is not None:
        num.delete()
    return HttpResponseRedirect('/welfareOffice/')

def welfare_get_actual_number(request):
    return HttpResponse("{}".format(get_actual_number(WelfareOfficeNumbersQueue)))

def welfare_get_available_number(request):
    return HttpResponse("{}".format(calculate_available_number(WelfareOfficeNumbersQueue)))

def welfare_reserve_number(request, login):
    return reserve_number(request, login, WelfareOfficeNumbersQueue)