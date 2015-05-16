from rest_framework import serializers

from main.models import Station


class StationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Station
