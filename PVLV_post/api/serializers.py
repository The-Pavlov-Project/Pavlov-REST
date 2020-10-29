from rest_framework.serializers import (
    ModelSerializer, RelatedField
)
from PVLV_user.api.serializers import UserSerializer
from PVLV_post.models import (
    Color,
    GeneratorSetting,
    Platform,
    Post,
)


class ColorSerializer(ModelSerializer):

    class Meta:
        model = Color
        fields = ['background', 'primary', 'text', 'is_dark']
        depth = 0


class GeneratorSettingsSerializer(ModelSerializer):

    colors = ColorSerializer(read_only=True, many=True)

    class Meta:
        model = GeneratorSetting
        exclude = ['parent']
        depth = 1


class PlatformSerializer(ModelSerializer):

    class Meta:
        model = Platform
        exclude = ['parent']


class PostSerializer(ModelSerializer):

    user = UserSerializer(read_only=True)
    operators = UserSerializer(read_only=True, many=True)
    platforms = PlatformSerializer(read_only=True, many=True)
    settings = GeneratorSettingsSerializer(read_only=True, many=True)

    class Meta:
        model = Post

        fields = [
            'user',
            'operators',
            'platforms',
            'settings',
        ]
