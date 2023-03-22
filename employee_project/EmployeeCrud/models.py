from django.db import models

# Create your models here.
Gender = [
    ('M', 'Male'),
    ('F', 'Female'),

]


class EmployeeModel(models.Model):
    EmpId = models.CharField(primary_key=True,max_length=100)
    Name = models.CharField(max_length=200)
    Email = models.EmailField(unique=True,)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=100,choices=Gender)
    PhoneNo = models.CharField(max_length=10)
    AddressDetails = models.TextField()
    HouseNo = models.CharField(max_length=200)
    Street = models.CharField(max_length=200)
    City = models.CharField(max_length=200)
    State = models.CharField(max_length=200)
    Photo = models.CharField(max_length=1000)
    objects = models.Manager


class projectmodel(models.Model):
    empId = models.ForeignKey(EmployeeModel,on_delete=models.CASCADE,related_name='project')
    Title = models.CharField(max_length=1000)
    description = models.TextField(max_length=1000)
    objects = models.Manager



class qualificationmodel(models.Model):
    empId = models.ForeignKey(EmployeeModel,on_delete=models.CASCADE,related_name='qualifications')
    qualificationName = models.TextField(max_length=1000)
    fromDate = models.DateField()
    toDate = models.DateField()
    percentage =models.IntegerField()
    objects = models.Manager
class Work_Experience(models.Model):
    empId = models.ForeignKey(EmployeeModel,on_delete=models.CASCADE,related_name='workExperience')
    workExperience = models.CharField(max_length=1000)
    CompanyName = models.CharField(max_length=200)
    FromDate = models.DateField()
    ToDate = models.DateField(max_length=200)
    CompanyAddress = models.CharField(max_length=200)