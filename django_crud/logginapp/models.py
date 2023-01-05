from django.db import models

# Create your models here.
from django.db import models


class loginmodel(models.Model):
    firstname = models.CharField(max_length=20, unique=True)
    lastname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    objects = models.Manager