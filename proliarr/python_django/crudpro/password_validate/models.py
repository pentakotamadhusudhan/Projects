from django.core.validators import RegexValidator
from django.db import models


class Validation(models.Model):
    first_name = models.CharField(max_length=30)

    #Last_name = RegexValidator(regex=r'^(?=.{3,12}$)(?![_.])(?!.*[_.]{2})[a-zA-Z]+(?<![_.])$',
     #                          message="last_name "
      #                                 "must string and should not be less than 3 and greater than 12")
    #     last_name = models.CharField(validators=[Last_name], max_length=30)
    last_name = models.CharField(max_length=30)
    Password = RegexValidator(regex=r"^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$",
                              message="password "
                                      "must contain 8 letters and a captITAL letter and a special character ")
    password = models.CharField(validators=[Password], max_length=30)
    objects = models.Manager
    """
    syntax is ?=.*{8,} minimum limit 8 lenght
    (?=.*[a-z]) small alphabhets kept in square brackets
    
    """