from rest_framework import viewsets

from main.models import Station
from restapi.serializers import StationSerializer
from rest_framework import filters

class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('full_name',)
