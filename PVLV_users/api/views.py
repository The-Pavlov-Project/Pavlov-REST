from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from django.http import HttpResponse

from PVLV_users.models import User
from .serializers import UsersSerializer


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

    @action(detail=False, methods=['GET'], name='Find User')
    def user(self, request, *args, **kwargs):
        user_id = request.GET.get('user_id')
        scope = request.GET.get('scope')
        return HttpResponse('{}{}'.format(user_id, scope))
