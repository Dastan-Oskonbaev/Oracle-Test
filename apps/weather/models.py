from django.db import models


class Weather(models.Model):
    city = models.CharField(max_length=255)
    temperature = models.FloatField()
    pressure = models.FloatField()
    wind_speed = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
