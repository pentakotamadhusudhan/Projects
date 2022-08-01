from django.db import models

# Create your models here.
class barmodel(models.Model):
    product_name = models.CharField(max_length=25)
    product_code = models.CharField(max_length=25)
    pack_code = models.CharField(max_length=25)
    bar_code = models.BinaryField(max_length=100)
    objects = models.Manager



class barreaddb(models.Model):
    bar_field = models.ImageField()