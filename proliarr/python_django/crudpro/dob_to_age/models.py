from django.db import models


class dobtable(models.Model):
    dob = models.DateField()
    Age = models.IntegerField()
    objects = models.Manager
