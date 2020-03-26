from pavlov import settings
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class User(AbstractUser):

    email = models.EmailField(unique=True)

    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    time_zone = models.IntegerField(default=0)
    gender = models.CharField(default='', max_length=100)
    age = models.IntegerField(default=0)
    country = models.IntegerField(default=0)
    vip_code = models.IntegerField(default=0)
    deep_logging = models.BooleanField(default=True)

    # auto regenerated, is the code to send as verification.
    verification_code = models.IntegerField(default=0)

    # the current game pass of the user
    game_pass = models.CharField(default='', max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
        Automatically create the User token once the user is created
    """
    if created:
        Token.objects.create(User=instance)
