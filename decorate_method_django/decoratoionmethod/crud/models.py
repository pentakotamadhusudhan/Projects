from django.db import models

# Create your models here.

class firstmodel(models.Model):
    Name = models.CharField(max_length=10)
    Mobile_number = models.BigIntegerField()
    Password = models.CharField(max_length=16)
    objects  =  models.Manager