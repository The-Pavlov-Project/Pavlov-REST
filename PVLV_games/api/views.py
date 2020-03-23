from rest_framework.viewsets import ModelViewSet

from PVLV_games.models import Game
from .serializers import GamesSerializer


class GamesModelViewSet(ModelViewSet):

    queryset = Game.objects.all()
    serializer_class = GamesSerializer
