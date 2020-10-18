from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from PVLV_auth.api.views import UserRegisterViewSet


urlpatterns = [
    path('login/', obtain_auth_token, name='api-login'),
    path('register/', UserRegisterViewSet.as_view(), name='api-register'),
]
