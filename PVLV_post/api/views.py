from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.viewsets import ReadOnlyModelViewSet


from PVLV_post.models import Color, PostGeneratorConfig

from .serializers import (
    ColorSerializer,
    PostGeneratorConfigsSerializer,
)


class ColorViewSet(ReadOnlyModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = (IsAdminUser,)


class PostGeneratorConfigsViewSet(ReadOnlyModelViewSet):
    queryset = PostGeneratorConfig.objects.all()
    serializer_class = PostGeneratorConfigsSerializer
    permission_classes = (IsAdminUser,)

    @action(detail=True, name='post-scope', methods=['GET'])
    def scope(self, request, user_id=None, scope=None):

        try:
            post_config = PostGeneratorConfig.objects.get(owner=user_id, scope=scope)
        except PostGeneratorConfig.DoesNotExist:
            return Response({'message': 'PostGeneratorConfigs does not exist'}, status=HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            return Response(PostGeneratorConfigsSerializer(post_config).data)

        elif request.method == 'PUT':
            _serializer = PostGeneratorConfigsSerializer(post_config, data=request.data, partial=True)
            _serializer.is_valid(raise_exception=True)
            _serializer.save()
            return Response(_serializer.data)
