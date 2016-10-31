from django.db import models

class Special(models.Model):
    created_user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    picture = models.FileField()

    def __str__(self):
        return str(self.title)

    @property
    def image_url(self):
        if self.picture:
            return self.picture.url
        return "http://images.clipartpanda.com/animated-question-mark-for-powerpoint-1256186461796715642question-mark-icon.svg.hi.png"
