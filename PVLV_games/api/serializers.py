from rest_framework.serializers import (
    ModelSerializer,
)
from PVLV_games.models import (
    Game,
    Plant,
)
from PVLV_games.api.plant.serializers import PlantSerializer


class GamesSerializer(ModelSerializer):

    plant = PlantSerializer()

    class Meta:
        model = Game
        exclude = []



