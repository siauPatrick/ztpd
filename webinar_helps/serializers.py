from rest_framework import serializers

from .models import Citizen, Species


class CitizenSerializer(serializers.ModelSerializer):
    # species = serializers.StringRelatedField(source='species.name')
    species = serializers.SerializerMethodField()

    class Meta:
        model = Citizen
        fields = ('name', 'species', 'gender', 'photo_url', 'fandom_url')

    def get_species(self, obj):
        try:
            species = obj.species
        except Species.DoesNotExist:
            species = None

        return species and species.name.capitalize()
