from django.db import models


class agetable(models.Model):
    date1 = models.DateField()
    date2 = models.DateField()
    diff = models.CharField(max_length=200, default=None)
    objects = models.Manager
