from rest_framework import filters, generics

from .models import Citizen
from .serializers import CitizenSerializer


class CitizenListAPIView(generics.ListAPIView):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
