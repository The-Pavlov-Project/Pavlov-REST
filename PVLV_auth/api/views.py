from rest_framework.generics import CreateAPIView

from PVLV_games.models import Game
from .serializers import UserRegistrationSerializer


class UserRegisterViewSet(CreateAPIView):

    queryset = Game.objects.all()
    serializer_class = UserRegistrationSerializer
