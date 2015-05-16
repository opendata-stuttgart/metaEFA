from rest_framework import routers
from django.conf.urls import patterns, include, url

from restapi.views import StationViewSet


router = routers.DefaultRouter()
router.register(r'station', StationViewSet)

urlpatterns = patterns(
    '',
    url(
        regex=r'v1/', view=include(router.urls)
    ),
)
