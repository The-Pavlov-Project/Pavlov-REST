from django.db import models
from django.utils import timezone


class Scope(models.TextChoices):
    TELEGRAM = 'T', 'Telegram'
    DISCORD = 'D', 'Discord'


class User(models.Model):

    email = models.EmailField()
    time_zone = models.IntegerField(default=0)
    gender = ''
    age = models.IntegerField(default=0)
    country = models.IntegerField(default=0)
    vip_code = models.IntegerField(default=0)
    deep_logging = models.BooleanField(default=True)
    suspended = models.BooleanField()

    # auto regenerated, is the code to send as verification.
    verification_code = models.IntegerField(default=0)

    # the current game pass of the user
    game_pass = models.CharField(default='', max_length=100)

    class Meta:
        ordering = []

    objects = models.Manager()


class UserApp(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
    )

    # identification key (user_id, scope)
    user_app_id = models.IntegerField(null=False)
    app_type = models.CharField(choices=Scope.choices, max_length=15)

    username = models.CharField(max_length=100)

    creation_timestamp = models.DateTimeField(default=timezone.now)
    last_seen = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = []

    objects = models.Manager()
