from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from main.models import Station
from restapi.serializers import StationSerializer
from rest_framework import filters
from main.utils import get_EFA_from_VVS, parse_efa


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'full_name')

    @detail_route()
    def departures(self, request, **kwargs):
        station = self.get_object()
        station_id = station.station_id
        return Response(parse_efa(get_EFA_from_VVS(station_id)))
