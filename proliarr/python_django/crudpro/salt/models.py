from django.db import models

# Create your models here.
class saltmodel(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=36)
    update_password = models.CharField(max_length=50)
    objects = models.Manager