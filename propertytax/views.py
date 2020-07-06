from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

from .models import PropertyTax
from .serializers import PropertyTaxRateSerializer
# Create your views here.


@api_view(['GET','POST'])
def getPropertyTax(request):
    if request.method=='GET':
        obj = PropertyTax.objects.all()
        serializer = PropertyTaxRateSerializer(obj, many=True)
        return Response(serializer.data)
    if request.method=="POST":
        propert_value= request.data.get('property_value')
        obj = PropertyTax.objects.only('property_tax')
        serializer = PropertyTaxRateSerializer(obj, many=True)
        newarray=[]

        for e in serializer.data:
                tax_amount = (e['property_tax'] /100 * int(propert_value))
                e.update({'tax_amount': tax_amount})
        return Response(serializer.data)

