from rest_framework.serializers import (
    ModelSerializer,
)
from PVLV_games.models import (
    Plant,
)


class PlantSerializer(ModelSerializer):

    class Meta:
        model = Plant
        exclude = []
