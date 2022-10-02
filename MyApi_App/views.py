from django.shortcuts import render
from .models import *
from .serializer import *
from .mypagination import *
from rest_framework.generics import ListAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend  # it's needs for Generic Filtering
from rest_framework import filters  # it's needs for search filter

# Create your views here.


class StudentListApi(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyPageNumberPagination

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Roll', 'Section']


class StudentCreateApi(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# we can use pagination by globally declaration build in pagination class in setting.py file
