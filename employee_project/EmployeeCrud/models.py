from django.db import models

# Create your models here.
Gender = [
    ('M', 'Male'),
    ('F', 'Female'),

]


class EmployeeModel(models.Model):
    EmpId = models.CharField(max_length=100,)
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
    # WorkExperience = models.CharField(max_length=1000)
    CompanyName = models.CharField(max_length=200)
    FromDate = models.DateField()
    ToDate = models.DateField(max_length=200)
    CompanyAddress = models.CharField(max_length=200)
    # Qualifications = models.ForeignKey(qualificationmodel,related_name='qualification',on_delete=models.CASCADE)
    QualificationName = models.CharField(max_length=200)
    Precentage = models.CharField(max_length=200)
    # Projects = models.ForeignKey(percentagemodel,related_name="project",on_delete=models.CASCADE)
    Title = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    Photo = models.CharField(max_length=1000)
    objects = models.Manager


class projectmodel(models.Model):
    empId = models.ForeignKey(EmployeeModel,on_delete=models.CASCADE,related_name='projects')
    Title = models.CharField(max_length=1000)
    description = models.TextField(max_length=1000)
    # objects = models.Manager



class qualificationmodel(models.Model):
    empId = models.ForeignKey(EmployeeModel,on_delete=models.CASCADE,related_name='qualification')
    qualificationName = models.TextField(max_length=1000)
    fromDate = models.DateField()
    toDate = models.DateField()
    percentage =models.IntegerField()
    # objects = models.Manager
