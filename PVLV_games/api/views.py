from rest_framework.viewsets import ModelViewSet

from PVLV_games.models import GamePass, GameSettings
from .serializers import GamePassSerializer, GameSettingsSerializer


class GamePassModelViewSet(ModelViewSet):
    queryset = GamePass.objects.all()
    serializer_class = GamePassSerializer


class GamesSettingsModelViewSet(ModelViewSet):
    queryset = GameSettings.objects.all()
    serializer_class = GameSettingsSerializer
