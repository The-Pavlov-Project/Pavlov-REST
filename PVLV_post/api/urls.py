from django.urls import path
from rest_framework import routers
from PVLV_post.api.views import ColorViewSet, PostGeneratorConfigsViewSet

router = routers.DefaultRouter()
router.register('', PostGeneratorConfigsViewSet)
router.register('detail/color', ColorViewSet)


urlpatterns = [
    path('<slug:name>/', PostGeneratorConfigsViewSet.as_view({
        'get': 'name',
        'put': 'name'
    })),
] + router.urls
