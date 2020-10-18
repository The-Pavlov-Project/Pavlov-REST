"""pavlov URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from PVLV_user.views import profile
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('PVLV_website.urls')),
    path('blog/', include('PVLV_website.blog.urls')),
    path('auth/', include('PVLV_auth.urls')),
    path('profile/', profile, name='profile'),

    # api endpoints
    path('api/auth/', include('PVLV_auth.api.urls')),
    path('api/chatwars/', include('PVLV_chatwars.urls')),
    path('api/g/', include('PVLV_games.urls')),
    path('api/platform/', include('PVLV_platform.urls')),
    path('api/post/', include('PVLV_post.urls')),
    path('api/user/', include('PVLV_user.api.urls')),

]

# serve media static in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
