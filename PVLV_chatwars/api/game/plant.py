from math import floor
from random import choices, randrange
from datetime import timedelta

from django.utils import timezone
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST


from PVLV_games.api.errors import PlantErrors, BillErrors


class PlantGame:

    MAX_PLANT = 160000

    def __init__(self, bill, plant):
        self.__bill = bill
        self.__plant = plant

        self.__min_time_to_pickup = timedelta(minutes=120)  # minimum time to have results in pick up
        self.__min_time_to_replant = timedelta(minutes=10)

    def __plant_value(self, bits):
        """
        Randomly calculate the success percentage
        - The user can have a multiplier success between 0% and 60%
        - Chosen by
        :param bits: the numbers of coins to plant
        """
        population = [1, 2, 3, 4, 5]
        weights = [0.3, 0.2, 0.2, 0.2, 0.1]
        main_value = choices(population, weights)[0] / 10  # get the item and convert the value as 0.x
        mv = main_value + (randrange(1, 9)/100) + 1

        self.__plant.planted_value = bits
        self.__plant.creation_timestamp = timezone.now()
        self.__plant.multiplier_value = mv
        self.__plant.is_planted = True

    def __calculate_hydration(self):
        """
        It will check the hydration level
        and if the plant will die for it
        :return: hydration level
        """
        t = timezone.now() - self.__plant.creation_timestamp
        h = t.seconds / 3600 + 1
        hydration_value = int(self.__plant.water_used * 10 / h)
        if not (3 < hydration_value < 17):
            self.__plant.is_dead = True
        return hydration_value

    def __calculate_profit(self):
        """
        t: time since the plant
        h: hours since the plant
        m: bits multiplier
        :return: the total bits gained
        """
        if self.__plant.is_dead:
            return int(self.__plant.planted_value / 2)

        if timezone.now() - self.__plant.creation_timestamp < self.__min_time_to_pickup:
            return self.__plant.planted_value

        t = timezone.now() - self.__plant.creation_timestamp
        h = t.seconds / 3600 + 1
        m = self.__plant.multiplier_value + h * 0.08
        bits = int(self.__plant.planted_value * m)
        return bits

    def wet(self, value: int):
        """
        Wet the bits, this will increase the multiplier value
        - check if the user has put a value to increment
        - too much water in a very short time will kill the bits
        - you will discover the status only on pick up or by checking

        - calculate the hydration value
        """

        if not self.__plant.is_planted:
            return Response(PlantErrors.NOTHING_PLANTED, status=HTTP_400_BAD_REQUEST)

        try:
            self.__bill.bits -= value * 10
        except ValueError:
            return Response(BillErrors.NO_MONEY, status=HTTP_400_BAD_REQUEST)

        self.__plant.water_used += value
        self.__plant.multiplier_value += value * 0.06

        self.__bill.save()
        self.__plant.save()
        return Response({
            'wet_times': value,
            'hydration_level': self.__calculate_hydration(),
        })

    def status(self):
        """
        Check the growth status of the bits

        hv: hydration value
        pv: planted value at the begin
        p: profit, value get if harvested
        w: num of times of -wet
        hp: hours passed since plant
        t: timestamp of plant
        """
        if not self.__plant.is_planted:
            return Response(PlantErrors.NOTHING_PLANTED, status=HTTP_400_BAD_REQUEST)

        return Response({
            'hydration_level': self.__calculate_hydration(),
            'planted_value': self.__plant.planted_value,
            'pick_value': self.__calculate_profit(),
            'water_used': self.__plant.water_used,
            'hours_since_plant': floor((timezone.now() - self.__plant.creation_timestamp).seconds / 3600),
            'planted_timestamp': self.__plant.creation_timestamp,
        })

    def pick(self):
        """
        Pick the bits up based on conditions
        - no planted stuff - return
        - if the right time is passed - pick up and multiply
        - no time is passed - just pick up
        """
        if not self.__plant.is_planted:
            return Response(data=PlantErrors.NOTHING_PLANTED, status=HTTP_400_BAD_REQUEST)

        else:
            """
            Pick the bits up and save them into the credit
            multiply if specified
            reset all the control values
            """
            bits = self.__calculate_profit()
            self.__bill.bits += bits
            res = {
                'planted_value': self.__plant.planted_value,
                'picked_value': bits,
                'is_dead': self.__plant.is_dead,
                'hours_since_plant': floor((timezone.now() - self.__plant.creation_timestamp).seconds / 3600),
                'planted_timestamp': self.__plant.creation_timestamp,
            }

            self.__bill.save()
            self.__plant.reset()
            return Response(res)

    def plant(self, value: int):
        """
            Plant a certain amount of bits
            Based on certain conditions
            - you already have stuff planted - return
            - wait before replant - cool down 10 min
            - nothing is planted - plant

            - only command - send the message that explain all
        """
        if self.__plant.is_planted:
            return Response(PlantErrors.ALREADY_PLANTED, status=HTTP_400_BAD_REQUEST)

        elif timezone.now() - self.__plant.harvest_timestamp < self.__min_time_to_replant:
            return Response(PlantErrors.REPLANT_TIMEOUT, status=HTTP_400_BAD_REQUEST)

        else:
            """
            - try to convert the bits value and plant them
            - sub user money from the bill
            - plant the bits
            """
            planted_max = False
            if value > self.MAX_PLANT:
                value = self.MAX_PLANT
                planted_max = True

            try:
                cost = int(value/3)
                self.__bill.bits -= value + cost
            except ValueError:
                return Response(BillErrors.NO_MONEY, status=HTTP_400_BAD_REQUEST)

            self.__plant_value(value)

            self.__bill.save()
            self.__plant.save()
            return Response({
                'planted_value': value,
                'plant_cost': cost,
                'planted_max': planted_max,
            })
