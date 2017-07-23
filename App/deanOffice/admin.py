from django.contrib import admin
from .models import Employee
from .models import Student
from .models import NumbersQueue

admin.site.register(Employee)
admin.site.register(Student)
admin.site.register(NumbersQueue)