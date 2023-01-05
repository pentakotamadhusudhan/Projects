from django.db import models

m=(('m','male'),
    ('f','female')
   )

# Create your models here.
class logintable(models.Model):
    first_name = models.CharField(max_length=25)
    second_name = models.CharField(max_length=25)
    username = models.CharField(max_length=25)
    gender = models.CharField(max_length=10,choices=m)
    password = models.CharField(max_length=36)
    email = models.EmailField()
    datetime = models.DateTimeField(auto_now=True)
    objects = models.Manager
    class Meta:
        db_table = 'pro1'