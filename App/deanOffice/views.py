from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.shortcuts import render
from .models import Student, DeanOfficeNumbersQueue, WelfareOfficeNumbersQueue
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, transaction
import hashlib

def check_login_password(login, password):
    student = Student.objects.get(studentId = login)
    if student != None and student.password == password:
        return True
    else:
        return False

def check_login(request, login, password):
    return HttpResponse("{}".format(check_login_password(login, password)))

def create_empty_student():
    student = Student()
    student.studentId = "---"
    student.firstName = "---"
    student.lastName = ""
    student.faculty = "---"
    student.groupId = "---"
    return student

def render_main_site(request, NumberQueueModel, next_number_view):
    num = NumberQueueModel.objects.first()
    if num is None:
        num = NumberQueueModel()
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

@transaction.atomic
def reserve_number(request, login, NumbersQueueModel):
    student = Student.objects.get(studentId = login)
    if student is None:
        return HttpResponse("Student not exist")

    num = NumbersQueueModel.objects.create(studentId = student)
    return HttpResponse("{}".format(num.numberId))

def dean_reserve_number(request, login, password):
    if check_login_password(login, password):
        return reserve_number(request, login, DeanOfficeNumbersQueue)
    else:
        return HttpResponse("Access Denied")

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

def welfare_reserve_number(request, login, password):
    if check_login_password(login, password):
        return reserve_number(request, login, WelfareOfficeNumbersQueue)
    else:
        return HttpResponse("Access Denied")
