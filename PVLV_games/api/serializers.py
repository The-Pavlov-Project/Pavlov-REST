from rest_framework.serializers import ModelSerializer
from PVLV_user.api.serializers import UserSerializer
from PVLV_games.models import (
    GamePass,
    GameSettings
)


class GamePassSerializer(ModelSerializer):

    class Meta:
        model = GamePass
        exclude = []


class GamePassInfoSerializer(ModelSerializer):

    created_by = UserSerializer(read_only=True)

    class Meta:
        model = GamePass
        exclude = []


class GameSettingsSerializer(ModelSerializer):

    class Meta:
        model = GameSettings
        exclude = []
