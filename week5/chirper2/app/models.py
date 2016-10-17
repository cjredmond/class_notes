from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

class Chirp(models.Model):
    body = models.CharField(max_length=140)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User')


    class Meta():
        ordering = ("-created",)

    def __str__(self):
        return self.body
    @property
    def score(self):
        return sum([chirp_obj.score for chirp_obj in self.vote_set.all()])

class Vote(models.Model):
    user = models.ForeignKey("auth.User")
    chirp = models.ForeignKey('app.Chirp')
    value = models.BooleanField()

    class Meta:
        unique_together = ("user", "chirp")

    def __str__(self):
        return "{} - {}".format(self.chirp.body, self.score)
    @property
    def score(self):
        if self.value:
            return 1
        return -1
