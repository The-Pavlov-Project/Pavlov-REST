from rest_framework.serializers import (
    ModelSerializer,
)
from PVLV_user.api.serializers import UserSerializer
from PVLV_post.models import (
    Color,
    PostGeneratorSubConfig,
    PostGeneratorConfig,
)


class ColorSerializer(ModelSerializer):

    class Meta:
        model = Color
        exclude = ['id']
        depth = 0


class PostGeneratorSubConfigSerializer(ModelSerializer):

    colors = ColorSerializer(read_only=True, many=True)

    class Meta:
        model = PostGeneratorSubConfig
        exclude = ['id']


class PostGeneratorConfigsSerializer(ModelSerializer):

    owners = UserSerializer(read_only=True, many=True)

    class Meta:
        model = PostGeneratorConfig
        exclude = []
        depth = 2
