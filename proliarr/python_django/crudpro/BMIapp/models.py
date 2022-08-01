from django.db import models

# Create your models here.
class bmimodel(models.Model):
    weight = models.IntegerField()
    height = models.IntegerField()
    BMI_value = models.IntegerField()
    objects=models.Manager