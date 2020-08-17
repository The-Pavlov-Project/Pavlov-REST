from django.db import models
from django.utils import timezone

from django.contrib.auth import get_user_model
from PVLV_games.models import GamePass

User = get_user_model()

creation_datetime = '01/01/2000 12:00:00'


class Factory(models.Model):
    """
    Upgradable factories
    generate value over time
    """
    last_pick = models.DateTimeField(default=timezone.datetime.strptime(creation_datetime, '%m/%d/%Y %H:%M:%S'))
    level = models.IntegerField(default=1)

    @staticmethod
    def create():
        factory = Factory()
        factory.save()
        return factory.id


class Army(models.Model):
    """
    To keep track of the user army
    """
    goblin = models.IntegerField(default=0)
    wizards = models.IntegerField(default=0)
    archers = models.IntegerField(default=0)
    assassins = models.IntegerField(default=0)

    objects = models.Manager()


class Game(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )
    game_pass = models.ForeignKey(
        GamePass,
        on_delete=models.CASCADE,
        null=True
    )
    created_at = models.DateTimeField(default=timezone.now)

    """
        Levels in the chat wars, you can gain or loose levels with the xp
    """
    xp = models.IntegerField(default=10)
    level = models.IntegerField(default=0)
    # prestige = models.IntegerField(default=0)

    """
        To track the plant data of the user
        The values that the user plant in the field to let them grow
    """
    _bits = models.IntegerField(default=10)
    bits_last_farm = models.DateTimeField(default=timezone.datetime.strptime(creation_datetime, '%m/%d/%Y %H:%M:%S'))
    bits_spent = models.IntegerField(default=0)  # automatically updated field

    # donations (give command)
    bits_received = models.IntegerField(default=0)
    bits_given_away = models.IntegerField(default=0)

    @property
    def bits(self):
        return self._bits

    @bits.setter
    def bits(self, value):
        """
        Check if the new value is under 0
        Keep track of the bits spent and earned
        Update the bits

        :param value: the new amount to set
        :raise: ValueError if the user don't have enough money
        """
        if value < 0:  # if the user don't have enough money for the transaction
            raise ValueError

        value = int(value)
        diff = self._bits - value

        # if diff is > 0; user has spent money
        if diff > 0:
            self.bits_spent += diff
        self._bits = value  # update the value in db

    plants = models.OneToOneField(
        Factory,
        related_name='plant',
        default=Factory.create,
        blank=True,
        on_delete=models.SET_DEFAULT
    )
    mines = models.OneToOneField(
        Factory,
        related_name='mines',
        default=Factory.create,
        blank=True,
        on_delete=models.SET_DEFAULT
    )

    objects = models.Manager()

    class Meta:
        # ordering = ['prestige']
        unique_together = ('user', 'game_pass')

    def __str__(self):
        return '{} - {}'.format(self.user, self.game_pass)
