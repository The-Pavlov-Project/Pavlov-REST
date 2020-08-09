from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Scope(models.TextChoices):
    TELEGRAM = 'T', 'Telegram'
    DISCORD = 'D', 'Discord'


class Languages(models.TextChoices):
    English = 'eng', 'English'
    Italian = 'ita', 'Italian'


class GuildPlatform(models.Model):
    platform = models.CharField(choices=Scope.choices, max_length=15)
    guild_platform_id = models.IntegerField(null=False)
    guild_name = models.CharField(max_length=25, default='Wonderland', blank=True)
    language = models.CharField(choices=Languages.choices, default=Languages.English.value, max_length=3, blank=True)

    bot_paused = models.BooleanField(default=False)
    bot_disabled = models.BooleanField(default=False)
    guild_pro = models.IntegerField(default=10, blank=True)

    prefix = models.CharField(max_length=5, default='.', blank=True)

    interaction_id = models.IntegerField(null=False, default=0, blank=True)

    class Meta:
        ordering = []
        unique_together = ('platform', 'guild_platform_id')

    objects = models.Manager()

    def __str__(self):
        return '{}-{}-{}'.format(self.platform, self.guild_name, self.guild_platform_id)


class UserPlatform(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    # identification key (user_platform_id, platform)
    platform = models.CharField(choices=Scope.choices, max_length=15)
    user_platform_id = models.IntegerField(default=0)
    user_platform_username = models.CharField(max_length=100, default='black_frog')
    last_seen = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        ordering = []
        unique_together = ('platform', 'user_platform_id')

    objects = models.Manager()

    def __str__(self):
        return '{}-{}-{}'.format(self.platform, self.user_platform_username, self.user_platform_id)


class GuildUserPlatform(models.Model):
    # unique key in db (guild_platform_id, user_platform_id)
    guild_platform = models.ForeignKey(GuildPlatform, on_delete=models.CASCADE)
    user_platform = models.ForeignKey(UserPlatform, on_delete=models.CASCADE)
    permissions = models.IntegerField(default=10, blank=True)

    join_at_timestamp = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        ordering = []
        unique_together = ('guild_platform', 'user_platform')

    objects = models.Manager()

    def __str__(self):
        return '{}-{}'.format(self.guild_platform.guild_name, self.user_platform.user_platform_username)
