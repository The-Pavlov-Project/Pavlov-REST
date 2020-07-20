from django.urls import path, include
from rest_framework import routers
from PVLV_platform.api.views import PlatformViewSet

router = routers.DefaultRouter()
router.register('', PlatformViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<slug:platform>/<int:guild_id>/', PlatformViewSet.as_view({'get': 'guild'})),
    path('<slug:platform>/<int:guild_id>/<int:user_id>/', PlatformViewSet.as_view({'get': 'user'})),
]
