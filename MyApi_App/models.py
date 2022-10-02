from django.db import models


# Create your models here.

class Student(models.Model):
    Name = models.CharField(max_length=300, blank=True, null=True)
    Roll = models.IntegerField()
    Section = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.Name
