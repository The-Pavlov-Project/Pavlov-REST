from django.db import models
from django.utils import timezone

from PVLV_users.models import User


class Plant(models.Model):
    """
        To track the plant data of the user
        The values that the user plant in the field to let them grow
    """
    creation_timestamp = models.DateTimeField(default=timezone.now)
    harvest_timestamp = models.DateTimeField(default=timezone.now)
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


class Bill(models.Model):
    """
        To track the plant data of the user
        The values that the user plant in the field to let them grow
    """
    _bits = models.IntegerField(default=10)
    last_bit_farm = models.DateTimeField(default=timezone.now)
    spent = models.IntegerField(default=0)
    given = models.IntegerField(default=0)

    objects = models.Manager()

    @classmethod
    def get_new(cls):
        return cls.objects.create().id

    def build_data(self):
        data = {
            'bits': self._bits,
            'last_bit_farm': self.last_bit_farm,
        }
        return data

    @property
    def bits(self):
        return self._bits

    @bits.setter
    def bits(self, value):
        """
        :param value: the new amount to set
        :raise: ValueError if the user don't have enough money
        """
        if value < 0:
            raise ValueError
        self._bits = int(value)


class Game(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )
    game_pass = models.CharField(default='', max_length=100)
    bill = models.OneToOneField(Bill, on_delete=models.CASCADE, default=Bill.get_new)
    plant = models.OneToOneField(Plant, on_delete=models.CASCADE, default=Plant.get_new)

    objects = models.Manager()
