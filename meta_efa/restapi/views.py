from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from main.models import Station
from restapi.serializers import StationSerializer
from rest_framework import filters
from main.utils import get_EFA_from_VVS


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('full_name',)

    @detail_route()
    def departures(self, request, **kwargs):
        station = self.get_object()
        station_id = station.station_id
        get_EFA_from_VVS(station_id)

        return Response(station_id)
