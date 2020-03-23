from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import Http404

from PVLV_games.models import Game, Plant
from .serializers import PlantSerializer

from .game.plant import PlantGame


class PlantViewSet(ViewSet):

    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

    @staticmethod
    def __plant(user, game_pass):
        game = Game.objects.get(user=user, game_pass=game_pass)
        return PlantGame(game.bill, game.plant)

    @action(detail=False, name='Plant')
    def plant(self, request, user=None, game_pass=None):
        try:
            p = self.__plant(user, game_pass)
        except ObjectDoesNotExist:
            raise Http404

        v = int(request.GET.get('value', 1))
        return p.plant(v)

    @action(detail=False, name='Status')
    def status(self, request, user=None, game_pass=None):
        try:
            p = self.__plant(user, game_pass)
        except ObjectDoesNotExist:
            raise Http404

        return p.status()

    @action(detail=False, name='Wet Plants')
    def wet(self, request, user=None, game_pass=None):
        try:
            p = self.__plant(user, game_pass)
        except ObjectDoesNotExist:
            raise Http404

        v = int(request.GET.get('value', 1))
        return p.wet(v)

    @action(detail=False, name='Pick Plants')
    def pick(self, request, user=None, game_pass=None):
        try:
            p = self.__plant(user, game_pass)
        except ObjectDoesNotExist:
            raise Http404

        return p.pick()

