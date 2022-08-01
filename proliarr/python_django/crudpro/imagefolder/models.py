from django.db import models


# Create your models here.
class Img(models.Model):
    name = models.CharField(max_length=10)

    myimage = models.ImageField(upload_to='images')
    objects = models.Manager
