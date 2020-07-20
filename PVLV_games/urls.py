from django.urls import path, include
from rest_framework import routers
from PVLV_games.api.views import GamesModelViewSet
from PVLV_games.api.plant.views import PlantViewSet

router = routers.DefaultRouter()
router.register('', GamesModelViewSet)

urlpatterns = [
    # path('web/<slug:username>/', user, name='user-home'),

    path('plant/<int:user>/<slug:game_pass>/plant/', PlantViewSet.as_view({'get': 'plant'})),
    path('plant/<int:user>/<slug:game_pass>/status/', PlantViewSet.as_view({'get': 'status'})),
    path('plant/<int:user>/<slug:game_pass>/wet/', PlantViewSet.as_view({'get': 'wet'})),
    path('plant/<int:user>/<slug:game_pass>/pick/', PlantViewSet.as_view({'get': 'pick'})),
]

urlpatterns += router.urls
