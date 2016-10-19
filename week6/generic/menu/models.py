from django.db import models

class Special(models.Model):
    created_by = models.ForeignKey('auth.User')
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.FloatField()

    def __str__(self):
        return self.title

ACCESS_LEVELS = [
    ('e', 'Employee'), ('o', 'Owner')
]

class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    access_level = models.CharField(max_length=1, choices=ACCESS_LEVELS)

    # @property
    # def is_owner(self):
    #     return self.access_level == 'o'
