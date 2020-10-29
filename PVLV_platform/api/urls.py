from django.urls import path
from rest_framework import routers
from PVLV_platform.api.views import PlatformModelViewSet, GuildPlatformModelViewSet, UserPlatformModelViewSet

router = routers.DefaultRouter()
router.register('', PlatformModelViewSet)
router.register('detail/guild', GuildPlatformModelViewSet)
router.register('detail/user', UserPlatformModelViewSet)


urlpatterns = [
    path('<slug:platform>/<int:guild_id>/<int:user_id>/', PlatformModelViewSet.as_view({'get': 'platform'})),
    path('detail/guild/<slug:platform>/<int:guild_id>/', GuildPlatformModelViewSet.as_view({
        'get': 'guild',
        'put': 'guild'
    })),
    path('detail/user/<slug:platform>/<int:user_id>/', UserPlatformModelViewSet.as_view({
        'get': 'user',
        'put': 'user',
    })),
] + router.urls
