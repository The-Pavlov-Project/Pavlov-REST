from django.urls import path
from rest_framework import routers
from PVLV_post.api.views import ColorViewSet, PostViewSet

router = routers.DefaultRouter()
router.register('', PostViewSet)
router.register('detail/color', ColorViewSet)


urlpatterns = [
    path('user/<int:user_id>/', PostViewSet.as_view({'get': 'user'})),
] + router.urls
