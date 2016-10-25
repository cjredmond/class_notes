from django.db import models

class Special(models.Model):
    name = models.CharField(max_length=48)
    price = models.FloatField()
    description = models.CharField(max_length=100)
