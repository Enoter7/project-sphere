from django.db import models

class City(models.Model):
    name = models.CharField(default = 'city', max_length = 50)
    latitude = models.FloatField(default = 0)
    longitude = models.FloatField(default=0)

