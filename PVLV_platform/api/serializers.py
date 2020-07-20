from rest_framework.serializers import (
    ModelSerializer,
)
from PVLV_platform.models import (
    UserPlatform,
    GuildPlatform,
)


class UserPlatformSerializer(ModelSerializer):

    class Meta:
        model = UserPlatform
        exclude = []


class GuildPlatformSerializer(ModelSerializer):

    class Meta:
        model = GuildPlatform
        exclude = []
