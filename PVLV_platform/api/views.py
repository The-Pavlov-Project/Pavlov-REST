from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from PVLV_platform.models import UserPlatform, GuildPlatform
from .serializers import UserPlatformSerializer, GuildPlatformSerializer


class PlatformViewSet(ModelViewSet):
    queryset = UserPlatform.objects.all()
    serializer_class = UserPlatformSerializer

    @action(detail=False, name='Find User')
    def guild(self, request, platform=None, guild_id=None):
        guild_platform = GuildPlatform.objects.get(platform=platform, guild_platform_id=guild_id)
        return Response(GuildPlatformSerializer(guild_platform).data)

    @action(detail=False, name='Find User Guild')
    def user(self, request, platform=None, guild_id=None, user_id=None):
        user_platform = UserPlatform.objects.get(
            platform=platform,
            guild_platform_id=guild_id,
            user_platform_id=user_id
        )
        return Response(UserPlatformSerializer(user_platform).data)
