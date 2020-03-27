from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
# local imports
from .serializers import (GeneralStatsSerializer, CountryStatsSerializer)
from .helpers.renderers import RequestJSONRenderer
from .helpers.pagination_helper import Pagination
from .helpers.scrap_data import fech_data
from .models import GeneralStats, CountryCases


class GeneralStatsAPIView(generics.GenericAPIView):

    renderer_classes = (RequestJSONRenderer,)
    serializer_class = GeneralStatsSerializer

    def get(self, request):
        """
        Get the general stats
        """
        queryset = GeneralStats.objects.all().order_by('-created_at').first()
        serializer = self.serializer_class(
            queryset, context={'request': request})

        return Response(serializer.data, status=status.HTTP_200_OK)


class ListSearchCountriesAPIView(viewsets.ReadOnlyModelViewSet):
    """
    List search country model
    """
    renderer_classes = (RequestJSONRenderer,)
    serializer_class = CountryStatsSerializer
    pagination_class = Pagination
    queryset = CountryCases.objects.all().order_by("-total_cases")
    filter_backends = (SearchFilter,)
    search_fields = ('country',)

    def search(self, request, *args, **kwargs):
        """
        search a country
        """
        return super().list(request, *args, **kwargs)


class FetchData(generics.GenericAPIView):

    renderer_classes = (RequestJSONRenderer,)

    def get(self, request):
        """
        Get the general stats
        """
        fech_data()
        return Response({"meassage": "Data fetched successfully"}, status=status.HTTP_200_OK)
