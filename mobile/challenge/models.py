from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Challenge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FileField(upload_to='images/', null=True, verbose_name="Image File")

    def __str__(self):
        return '{}'.format(self.name)


class Video(models.Model):
    name = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/', null=True, verbose_name="Video File")
    image = models.FileField(upload_to='images/', null=True, verbose_name="Image File")
    challenge = models.ForeignKey(Challenge,related_name='videos', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)