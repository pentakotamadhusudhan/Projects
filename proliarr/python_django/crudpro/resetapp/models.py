from django.db import models


# Create your models here.
class resetmodel(models.Model):
    username = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    new_password = models.CharField(max_length=25)
    re_type_password = models.CharField(max_length=25)
    objects = models.Manager
