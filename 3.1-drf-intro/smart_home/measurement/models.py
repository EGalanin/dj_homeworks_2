from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=255, verbose_name='Описание датчика')


class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sensors = models.ForeignKey(Sensor, on_delete=models.CASCADE, null=True, related_name='measurements')
