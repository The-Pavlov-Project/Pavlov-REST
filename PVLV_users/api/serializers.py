from rest_framework.serializers import (
    ModelSerializer,
)
from PVLV_users.models import (
    User,
)


class UsersSerializer(ModelSerializer):

    class Meta:
        model = User
        exclude = []
