from django.db import models


# Create your models here.
class studentmodel(models.Model):
    student_name = models.CharField(max_length=20)
    student_age = models.IntegerField()
    objects = models.Manager



class peoplemodel(models.Model):
    name = models.CharField(max_length=20,null=True,unique=True)
    # name=employeemodel.objects.get(employee_name)
    age = models.IntegerField()
    objects = models.Manager

class employeemodel(models.Model):
    employee_name = models.ManyToManyField(peoplemodel)
    emp_number = models.IntegerField()
    objects = models.Manager
