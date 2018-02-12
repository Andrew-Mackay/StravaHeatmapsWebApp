from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone
from time import time
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username


def get_upload_file_name(instance, filename):
    return "gpx_files/%s_%s" % (str(time()).replace('.', '_'), filename)


class Activity(models.Model):
    sid = models.CharField(primary_key=True,max_length=10,default=uuid.uuid4)
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    gpxFile = models.FileField(upload_to=get_upload_file_name, default="")
    created =  models.DateTimeField(default=timezone.now)
