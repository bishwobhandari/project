from rest_framework import serializers
from .models import PropertyTax

class PropertyTaxRateSerializer(serializers.ModelSerializer):
    class Meta:
        model=PropertyTax
        fields='__all__'
