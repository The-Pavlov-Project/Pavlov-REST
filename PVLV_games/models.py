from django.db import models
from django.utils import timezone

from django.contrib.auth import get_user_model

User = get_user_model()

"""
    class Army(models.Model):
        goblin = models.IntegerField(default=0)
        wizards = models.IntegerField(default=0)
        archers = models.IntegerField(default=0)
        assassins = models.IntegerField(default=0)
    
        objects = models.Manager()
    
        @classmethod
        def get_new(cls):
            return cls.objects.create().id
    
    
    class Fight(models.Model):
        is_fight = models.CharField(default='', max_length=100)
    
        objects = models.Manager()
    
        @classmethod
        def get_new(cls):
            return cls.objects.create().id
"""


class Plant(models.Model):
    """
        To track the plant data of the user
        The values that the user plant in the field to let them grow
    """

    datetime_str = '01/01/2000 12:00:00'

    creation_timestamp = models.DateTimeField(default=timezone.datetime.strptime(datetime_str, '%m/%d/%Y %H:%M:%S'))
    harvest_timestamp = models.DateTimeField(default=timezone.datetime.strptime(datetime_str, '%m/%d/%Y %H:%M:%S'))
    is_planted = models.BooleanField(default=False)
    is_dead = models.BooleanField(default=False)
    planted_value = models.IntegerField(default=0)
    water_used = models.IntegerField(default=1)
    multiplier_value = models.FloatField(default=0.01)

    objects = models.Manager()

    def reset(self):
        self.harvest_timestamp = timezone.now()
        self.is_planted = False
        self.is_dead = False
        self.planted_value = 0
        self.water_used = 1
        self.multiplier_value = 0.01
        self.save()

    @classmethod
    def get_new(cls):
        return cls.objects.create().id


class Army(models.Model):
    """
        To keep track of the user army
    """
    is_planted = models.BooleanField(default=False)
    is_dead = models.BooleanField(default=False)
    planted_value = models.IntegerField(default=0)
    water_used = models.IntegerField(default=1)
    multiplier_value = models.FloatField(default=0.01)


class GamePass(models.Model):
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )
    game_pass = models.CharField(default='', max_length=20, unique=True)
    title = models.CharField(default='My Game Pass', max_length=40)
    description = models.CharField(default='Created to play with my friend', max_length=120)
    created_at = models.DateTimeField(default=timezone.now)

    objects = models.Manager()

    def __str__(self):
        return self.game_pass


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
    game_pass_join_at = models.DateTimeField(default=timezone.now)

    """
        Levels in the chat wars, you can gain or loose levels with the xp
    """
    xp = models.IntegerField(default=10)
    level = models.IntegerField(default=0)

    """
        To track the plant data of the user
        The values that the user plant in the field to let them grow
    """
    _bits = models.IntegerField(default=10)
    bits_last_farm = models.DateTimeField(default=timezone.now)
    bits_spent = models.IntegerField(default=0)
    bits_earned = models.IntegerField(default=0)
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
        if value < 0:
            raise ValueError

        value = int(value)

        diff = self._bits - value
        if diff > 0:
            self.bits_earned += (diff * -1)
        else:
            self.bits_spent += diff

        self._bits = value

    def build_data(self):
        data = {
            'bits': self._bits,
            'last_bit_farm': self.bits_last_farm,
        }
        return data

    plant = models.OneToOneField(Plant, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return '{} - {}'.format(self.user, self.game_pass)
