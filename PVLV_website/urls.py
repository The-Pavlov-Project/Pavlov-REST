from django.urls import path, include
from .views import (
    home,
    dashboard,
)
from PVLV_post.views import post_update

urlpatterns = [
    path('', home, name='home'),
    path('console/', dashboard, name='console'),
    path('console/post/', post_update, name='console-post'),

    # sub-apps
    path('blog/', include('PVLV_website.blog.urls')),
]
