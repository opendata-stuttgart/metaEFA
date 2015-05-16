from rest_framework import serializers

from main.models import Station
from restapi.utils import (
    dromeda_to_underscore,
    underscore_to_dromeda,
)


class AbstractDromedaSerializer(serializers.ModelSerializer):
    """Converts all incoming variable names from dromeda case to underscore an outgoing backwards"""

    def to_internal_value(self, data):
        for key in list(data.keys()):
            data[dromeda_to_underscore(key)] = data.pop(key)
        return super().to_internal_value(data)

    def to_representation(self, obj):
        data = super().to_representation(obj)
        for key in list(data.keys()):
            data[underscore_to_dromeda(key)] = data.pop(key)
        return data


class StationSerializer(AbstractDromedaSerializer):

    class Meta:
        model = Station
