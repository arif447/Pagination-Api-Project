from django.contrib import admin
from .models import *


class StudentList(admin.ModelAdmin):
    list_display = ['Name', 'Roll', 'Section']

    class Meta:
        model = Student


# Register your models here.

admin.site.register(Student, StudentList)
