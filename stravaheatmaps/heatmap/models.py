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
