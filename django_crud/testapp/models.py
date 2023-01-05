from django.db import models

# Create your models here.
class form(models.Model):
    name = models.CharField(max_length=25)
    second_name = models.CharField(max_length=25)
    dept = models.CharField(max_length=25)
    objects = models.Manager