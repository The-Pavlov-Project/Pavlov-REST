from django.urls import path, include
from rest_framework import routers

from PVLV_user.api.views import UserViewSet

router = routers.DefaultRouter()
router.register('', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
# path('user/', UserViewSet.as_view(), name='user'),
]
