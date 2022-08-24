from django.db import models


# Create your models here.
class Details(models.Model):
    name = models.CharField(max_length=100, unique=True)
    age = models.IntegerField()
    address = models.TextField(max_length=255)
    password = models.CharField(max_length=10)
    time=models.CharField(max_length=50)
    objects = models.Manager
