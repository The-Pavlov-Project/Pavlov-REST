from django.urls import path
from rest_framework import routers
from PVLV_chatwars.api.views import (
    GamesModelViewSet, TransferApiView, PayApiView
)

router = routers.DefaultRouter()
router.register('', GamesModelViewSet)

urlpatterns = [
    path('<slug:game_pass>/<int:user_id>/', GamesModelViewSet.as_view({
        'get': 'game_pass',
        'put': 'game_pass'
    })),

    path('<slug:game_pass>/<int:user_id>/transfer/', TransferApiView.as_view()),
    path('<slug:game_pass>/<int:user_id>/pay/', PayApiView.as_view()),
] + router.urls
