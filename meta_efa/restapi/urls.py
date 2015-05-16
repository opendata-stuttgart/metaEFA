from rest_framework import routers
from django.conf.urls import patterns, include, url


router = routers.DefaultRouter()


urlpatterns = patterns(
    '',
    url(
        regex=r'v1/^', view=include(router.urls)
    ),
)
