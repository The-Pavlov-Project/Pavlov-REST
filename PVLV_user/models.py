from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    email = models.EmailField(unique=True)

    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    time_zone = models.IntegerField(default=0)
    gender = models.CharField(default='Custom', max_length=100)
    age = models.IntegerField(default=0)
    country = models.IntegerField(default=0)
    vip_code = models.IntegerField(default=0)
    deep_logging = models.BooleanField(default=True)

    # auto regenerated, is the code to send as verification.
    verification_code = models.IntegerField(default=0)

    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['username']
