from rest_framework import serializers
from django.core.validators import MinValueValidator
from .models import CountryCases, GeneralStats


class CountryStatsSerializer(serializers.ModelSerializer):
    """Serializers for creating and retrieving all countries stats"""

    id = serializers.CharField(read_only=True)


    class Meta:
        model = CountryCases
        fields = ('__all__')


class GeneralStatsSerializer(serializers.ModelSerializer):
    """Serializers for creating and retrieving general stats"""
    id = serializers.CharField(read_only=True)


    class Meta:
        model = GeneralStats
        fields = ('__all__')
