from rest_framework import filters, generics

from .models import Citizen
from .serializers import CitizenSerializer


class CitizenListAPIView(generics.ListAPIView):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('species_id',)
    ordering = ('species_id',)
