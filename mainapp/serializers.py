from rest_framework import serializers
from .models import pokemoncenters
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class pokemoncenterslocationSerializer(GeoFeatureModelSerializer):
    """ A class to serialize locations as GeoJSON compatible data """

    class Meta:
        model = pokemoncenters
        geo_field = "location"
        fields = '__all__'

class pokemoncentersSerializer(serializers.ModelSerializer):
    class Meta:
        model = pokemoncenters
        fields = '__all__'
