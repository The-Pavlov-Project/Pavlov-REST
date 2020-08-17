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
from pavlov.views import pavlov_home


urlpatterns = [
    path('', pavlov_home),
    path('admin/', admin.site.urls),
    path('auth/', include('PVLV_auth.urls')),
    path('chatwars/', include('PVLV_chatwars.urls')),
    path('g/', include('PVLV_games.urls')),
    path('platform/', include('PVLV_platform.urls')),
    path('user/', include('PVLV_user.urls')),
]
