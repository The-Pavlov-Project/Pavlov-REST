from rest_framework.generics import CreateAPIView

from PVLV_user.models import User
from .serializers import UserRegistrationSerializer


class UserRegisterViewSet(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
