from django.db import models


# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length=10)
    department=models.CharField(max_length=10)
    password = models.CharField(max_length=16)
    objects = models.Manager

    def get_name(self):
        result = {'name':self.name,
                  'department':self.department,
                  'password':self.password}
        return result