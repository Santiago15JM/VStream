from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=255)
    uploader = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    fileName = models.CharField(max_length=255)


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    video = models.ForeignKey(Video, on_delete=models.DO_NOTHING)
