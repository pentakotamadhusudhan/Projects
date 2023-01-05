from django.db import models


# Create your models here.
class table(models.Model):
    currency = models.IntegerField()
    currency_word = models.CharField(max_length=25)
    objects = models.Manager
