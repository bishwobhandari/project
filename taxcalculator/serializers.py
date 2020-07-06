from rest_framework import serializers
from .models import TaxRates

class TaxRateSerializer(serializers.ModelSerializer):
    class Meta:
        model=TaxRates
        fields='__all__'
