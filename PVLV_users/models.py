from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Scope(models.TextChoices):
    TELEGRAM = 'T', 'Telegram'
    DISCORD = 'D', 'Discord'


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

    def __str__(self):
        return '{}-{}'.format(self.app_type, self.username)
