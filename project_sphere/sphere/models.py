from django.db import models

class City(models.Model):
    name = models.CharField(default = 'city', max_length = 50)

