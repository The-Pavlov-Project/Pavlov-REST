from django.db import models
from django.utils import timezone
from datetime import datetime

from django.contrib.auth import get_user_model

User = get_user_model()


class Mine(models.Model):
    last_pick = models.IntegerField(default=0)
    wizards = models.IntegerField(default=0)
    archers = models.IntegerField(default=0)
    assassins = models.IntegerField(default=0)

    objects = models.Manager()

    @classmethod
    def get_new(cls):
        return cls.objects.create().id