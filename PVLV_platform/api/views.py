from django.core.exceptions import SuspiciousOperation

from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND

from PVLV_platform.models import UserPlatform, GuildPlatform, GuildUserPlatform

from .serializers import (
    UserPlatformSerializer,
    GuildPlatformSerializer,
    GuildUserPlatformFullSerializer,
    GuildUserPlatformSerializer,
)


class PlatformModelViewSet(ModelViewSet):
    queryset = GuildUserPlatform.objects.all()
    serializer_class = GuildUserPlatformSerializer

    @action(detail=False, name='Get Guild User', methods=['GET', 'PUT'])
    def platform(self, request, platform=None, guild_id=None, user_id=None):
        platform = platform.upper()

        try:
            guild_user_platform = GuildUserPlatform.objects.get(
                guild_platform=GuildPlatform.objects.get(guild_platform_id=guild_id, platform=platform).id,
                user_platform=UserPlatform.objects.get(user_platform_id=user_id, platform=platform).id,
            )
        except GuildPlatform.DoesNotExist:
            return Response({'message': 'GuildPlatform does not exist'}, status=HTTP_404_NOT_FOUND)
        except UserPlatform.DoesNotExist:
            return Response({'message': 'UserPlatform does not exist'}, status=HTTP_404_NOT_FOUND)
        except GuildUserPlatform.DoesNotExist:
            return Response({'message': 'GuildUserPlatform does not exist'}, status=HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            return Response(GuildUserPlatformFullSerializer(guild_user_platform).data)

        elif request.method == 'PUT':
            _serializer = GuildUserPlatformFullSerializer(guild_user_platform, data=request.data, partial=True)
            _serializer.is_valid(raise_exception=True)
            _serializer.save()
            return Response(_serializer.data)


class GuildPlatformModelViewSet(ModelViewSet):
    queryset = GuildPlatform.objects.all()
    serializer_class = GuildPlatformSerializer

    @action(detail=True, name='Get User', methods=['GET', 'PUT'])
    def guild(self, request, platform=None, guild_id=None):
        platform = platform.upper()

        try:
            guild_platform = GuildPlatform.objects.get(platform=platform, guild_platform_id=guild_id)
        except GuildPlatform.DoesNotExist:
            return Response({'message': 'GuildPlatform does not exist'}, status=HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            return Response(GuildPlatformSerializer(guild_platform).data)

        elif request.method == 'PUT':
            _serializer = GuildPlatformSerializer(guild_platform, data=request.data, partial=True)
            _serializer.is_valid(raise_exception=True)
            _serializer.save()
            return Response(_serializer.data)


class UserPlatformModelViewSet(ModelViewSet):
    queryset = UserPlatform.objects.all()
    serializer_class = UserPlatformSerializer

    @action(detail=True, name='User', methods=['GET', 'PUT'])
    def user(self, request, platform=None, user_id=None):
        platform = platform.upper()

        try:
            user_platform = UserPlatform.objects.get(platform=platform, user_platform_id=user_id)
        except UserPlatform.DoesNotExist:
            return Response({'message': 'UserPlatform does not exist'}, status=HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            return Response(UserPlatformSerializer(user_platform).data)

        elif request.method == 'PUT':
            _serializer = UserPlatformSerializer(user_platform, data=request.data, partial=True)
            _serializer.is_valid(raise_exception=True)
            _serializer.save()
            return Response(_serializer.data)
