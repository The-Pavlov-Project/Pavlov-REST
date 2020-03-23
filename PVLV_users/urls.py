from django.urls import path, include
from rest_framework import routers
from PVLV_users.api.views import UsersViewSet

router = routers.DefaultRouter()
router.register('', UsersViewSet)

urlpatterns = [
    path('v1/', include(router.urls))
]

# urlpatterns += router.urls
