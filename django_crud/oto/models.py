from django.db import models
from django.contrib.auth.models import User


class main1(models.Model):
    UserName = models.CharField(max_length=70)
    Password = models.CharField(max_length=70)



class main2(models.Model):
    name = models.ForeignKey(main1, on_delete=models.CASCADE,null=True)
    first_name = models.CharField(max_length=70)
    second_name = models.CharField(max_length=70)
    DOB = models.DateField()
    objects = models.Manager
