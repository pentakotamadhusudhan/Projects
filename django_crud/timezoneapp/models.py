from django.db import models
import zoneinfo
import calendar


class timezonemodel(models.Model):
    TIMEZONE_CHOICES = ((x, x) for x in sorted(zoneinfo.available_timezones(), key=str.lower))
    timezone = models.CharField("Timezone", choices=TIMEZONE_CHOICES, max_length=250, default='Etc/GMT+2')
    DateTime = models.DateTimeField(auto_now_add=True)
    objects = models.Manager
