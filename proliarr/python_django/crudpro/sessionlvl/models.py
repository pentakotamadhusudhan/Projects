from django.db import models

# Create your models here.
from django.db import models


class pagemodel(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    password = models.CharField(max_length=36)

    objects = models.manager


class employee(models.Model):
    emp_name = models.CharField(max_length=20)
    emp_age = models.IntegerField()
    password = models.CharField(max_length=25)
    objects = models.Manager


class student(models.Model):
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    objects = models.Manager
