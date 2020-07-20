from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Scope(models.TextChoices):
    TELEGRAM = 'T', 'Telegram'
    DISCORD = 'D', 'Discord'


class GuildPlatform(models.Model):
    platform = models.CharField(choices=Scope.choices, max_length=15)
    guild_platform_id = models.IntegerField(null=False)
    name = models.CharField(max_length=25, default='Undercover Spy')

    bot_paused = models.BooleanField(default=False)
    bot_disabled = models.BooleanField(default=False)

    prefix = models.CharField(max_length=5, default='.')

    interaction_id = models.IntegerField(null=False, default=0)

    objects = models.Manager()

    def __str__(self):
        return '{}-{}'.format(self.platform, self.name)


class UserPlatform(models.Model):

    # unique key in db (user, platform)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
    )

    # identification key (user_platform_id, platform)
    user_platform_id = models.IntegerField(null=False)
    guild_platform_id = models.IntegerField(null=False)
    platform = models.CharField(choices=Scope.choices, max_length=15)

    username = models.CharField(max_length=100)

    creation_timestamp = models.DateTimeField(default=timezone.now)
    last_seen = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = []
        unique_together = ('user', 'platform',)

    objects = models.Manager()

    def __str__(self):
        return '{}-{}'.format(self.platform, self.username)
