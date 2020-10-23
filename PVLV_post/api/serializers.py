from rest_framework.serializers import (
    ModelSerializer,
)
from PVLV_user.api.serializers import UserSerializer
from PVLV_post.models import (
    Color,
    PostGeneratorConfig,
)


class ColorSerializer(ModelSerializer):

    class Meta:
        model = Color
        exclude = ['id']
        depth = 0


class PostGeneratorConfigsSerializer(ModelSerializer):

    owners = UserSerializer(read_only=True, many=True)

    class Meta:
        model = PostGeneratorConfig
        exclude = []
        depth = 2
