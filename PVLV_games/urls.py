from django.urls import path
from rest_framework import routers
from PVLV_games.api.views import GamePassModelViewSet, GamesSettingsModelViewSet

router = routers.DefaultRouter()
router.register('settings', GamesSettingsModelViewSet)
router.register('gamepass', GamePassModelViewSet)

urlpatterns = [

] + router.urls
