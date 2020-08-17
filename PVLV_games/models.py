from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class GamePass(models.Model):
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )
    code = models.CharField(default='', max_length=20, unique=True)
    title = models.CharField(default='My Game Pass', max_length=40)
    description = models.CharField(default='Created to play with my friend', max_length=120)
    created_at = models.DateTimeField(default=timezone.now)

    # if the game pass is active
    is_active = models.BooleanField(default=True)
    # password to join the game pass
    password = models.CharField(default='', max_length=20)

    objects = models.Manager()

    def __str__(self):
        return self.code


class GameSettings(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    game_pass = models.ForeignKey(
        GamePass,
        on_delete=models.SET_NULL,
        null=True
    )

    objects = models.Manager()

    def __str__(self):
        return '{} - {}'.format(self.user.username, self.game_pass.code)
