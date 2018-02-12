from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username



class Activity(models.Model):
    sid = models.CharField(primary_key=True,max_length=10,default=uuid.uuid4)
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


# YOU ARE HERE
class Point(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    lat = models.FloatField()
    lng = models.FloatField()
