from django.core.exceptions import SuspiciousOperation

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND

from PVLV_post.models import Color, PostGeneratorSubConfig, PostGeneratorConfig

from .serializers import (
    ColorSerializer,
    PostGeneratorSubConfigSerializer,
    PostGeneratorConfigsSerializer,
)


class ColorViewSet(ReadOnlyModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class PostGeneratorSubConfigViewSet(ReadOnlyModelViewSet):
    queryset = PostGeneratorSubConfig.objects.all()
    serializer_class = PostGeneratorSubConfigSerializer


class PostGeneratorConfigsViewSet(ReadOnlyModelViewSet):
    queryset = PostGeneratorConfig.objects.all()
    serializer_class = PostGeneratorConfigsSerializer

    @action(detail=True, name='Get Generator Name', methods=['GET', 'PUT'])
    def name(self, request, name=None):

        try:
            post_config = PostGeneratorConfig.objects.get(name=name)
        except PostGeneratorConfig.DoesNotExist:
            return Response({'message': 'PostGeneratorConfigs does not exist'}, status=HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            return Response(PostGeneratorConfigsSerializer(post_config).data)

        elif request.method == 'PUT':
            _serializer = PostGeneratorConfigsSerializer(post_config, data=request.data, partial=True)
            _serializer.is_valid(raise_exception=True)
            _serializer.save()
            return Response(_serializer.data)
