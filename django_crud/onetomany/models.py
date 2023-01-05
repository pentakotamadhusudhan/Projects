from django.db import models


# Create your models here.
class main(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    objects=models.Manager

class nextform(models.Model):
    first_name = models.OneToOneField(main, on_delete=models.CASCADE,null=True)
    ph_no = models.IntegerField()
    password = models.IntegerField(null=True)
    objects = models.Model

