from rest_framework.serializers import (
    ModelSerializer,
)
from PVLV_user.api.serializers import UserSerializer
from PVLV_platform.models import (
    UserPlatform,
    GuildPlatform,
    GuildUserPlatform,
)


class UserPlatformSerializer(ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = UserPlatform
        exclude = []
        depth = 1


class GuildPlatformSerializer(ModelSerializer):

    class Meta:
        model = GuildPlatform
        exclude = []


class GuildUserPlatformFullSerializer(ModelSerializer):

    user_platform = UserPlatformSerializer()
    guild_platform = GuildPlatformSerializer()

    class Meta:
        model = GuildUserPlatform
        exclude = []
        depth = 1


class GuildUserPlatformSerializer(ModelSerializer):

    class Meta:
        model = GuildUserPlatform
        exclude = []
        depth = 0
