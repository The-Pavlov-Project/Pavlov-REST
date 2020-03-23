from rest_framework.serializers import (
    ModelSerializer,
)
from PVLV_games.models import (
    Game,
)


class GamesSerializer(ModelSerializer):

    class Meta:
        model = Game
        exclude = []
        depth = 1


