from django.urls import path
from .views import StudentListApi, StudentCreateApi

urlpatterns = [
     path('list/', StudentListApi.as_view()),
     path('create/', StudentCreateApi.as_view()),
]

