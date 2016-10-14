from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

class Chirp(models.Model):
    body = models.CharField(max_length=140)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User')

    class Meta():
        ordering = ("-created",)
