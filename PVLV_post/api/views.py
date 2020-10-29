from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.viewsets import ReadOnlyModelViewSet


from PVLV_post.models import Color, Post

from .serializers import (
    ColorSerializer,
    PostSerializer,
)


class ColorViewSet(ReadOnlyModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = (IsAdminUser,)


class PostViewSet(ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (IsAdminUser,)

    @action(detail=True, name='post-scope', methods=['GET'])
    def user(self, request, user_id=None):

        try:
            post_config = Post.objects.get(user=user_id)
        except Post.DoesNotExist:
            return Response({'message': 'PostGeneratorConfigs does not exist'}, status=HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            return Response(PostSerializer(post_config).data)
