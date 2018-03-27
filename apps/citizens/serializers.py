from rest_framework import serializers

from .models import Citizen


class CitizenSerializer(serializers.ModelSerializer):
    species = serializers.StringRelatedField(source='species.name')
    # species = serializers.SerializerMethodField(source='pecies.name')

    class Meta:
        model = Citizen
        fields = ('name', 'species', 'gender', 'photo_url', 'fandom_url', 'creation_date')

    def get_species(self, obj):
        return obj.species.name.capitalize()
