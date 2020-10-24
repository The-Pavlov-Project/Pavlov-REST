from django.urls import path
from rest_framework import routers
from PVLV_post.api.views import ColorViewSet, PostGeneratorConfigsViewSet

router = routers.DefaultRouter()
router.register('', PostGeneratorConfigsViewSet)
router.register('detail/color', ColorViewSet)


urlpatterns = [
    path('<int:user_id>/<slug:scope>/', PostGeneratorConfigsViewSet.as_view({'get': 'scope'})),
] + router.urls
