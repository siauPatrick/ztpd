from rest_framework import serializers

from .models import Citizen


class CitizenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citizen
        fields = ('name', 'species', 'gender', 'photo_url', 'fandom_url', 'creation_date')
