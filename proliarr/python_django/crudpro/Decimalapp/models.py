from django.db import models

# Create your models here.
class Decimalmodel(models.Model):
    number = models.FloatField()
    digits = models.IntegerField()
    decimal_value = models.CharField(max_length=100)
    objects=models.Manager