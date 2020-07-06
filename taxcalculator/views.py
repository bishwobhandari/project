from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

from .models import TaxRates
from .serializers import TaxRateSerializer
# Create your views here.


@api_view(['GET','POST'])
def getTaxRate(request):
    if request.method=='GET':
        obj = TaxRates.objects.all()
        serializer = TaxRateSerializer(obj, many=True)
        return Response(serializer.data)
    if request.method=="POST":
        salary= request.data.get('salary')
        obj = TaxRates.objects.only('tax_rate')
        serializer = TaxRateSerializer(obj, many=True)
        newarray=[]
        base_amount = 17000
        taxed_amount=0
        salary_base_amount=int(salary)-base_amount
        for e in serializer.data:
            if e['tax_rate'] != 0:
                taxed_amount = 720+(e['tax_rate'] /100 * salary_base_amount)
                amount_after_tax=int(salary)-taxed_amount
                e.update({'salary_after_tax': int(amount_after_tax)})
            else:
                e.update({'salary_after_tax':salary})
        return Response(serializer.data)

