from django.urls import path, include
from .views import (
    home,
    dashboard,
)
from PVLV_post.views import post

urlpatterns = [
    path('', home, name='home'),
    path('console/', dashboard, name='console'),
    path('console/post', post, name='post'),

    # sub-apps
    path('blog/', include('PVLV_website.blog.urls')),
]
