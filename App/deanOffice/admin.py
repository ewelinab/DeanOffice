from django.contrib import admin
from .models import Student, DeanOfficeNumbersQueue, WelfareOfficeNumbersQueue

admin.site.register(Student)
admin.site.register(DeanOfficeNumbersQueue)
admin.site.register(WelfareOfficeNumbersQueue)