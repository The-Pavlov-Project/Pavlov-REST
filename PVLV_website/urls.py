from django.urls import path, include
from .views import (
    home,
)

urlpatterns = [
    path('', home, name='home'),
    # path('about/', about, name='about'),

    # sub-apps
    path('blog/', include('PVLV_website.blog.urls')),
]
