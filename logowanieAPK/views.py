import requests
from django.http import JsonResponse
from .models import ExchangeRate
from rest_framework import generics
from .serializers import ExchangeRateSerializer

def fetch_exchange_rates(request):
    response = requests.get('https://api.nbp.pl/api/exchangerates/tables/A?format=json')
    data = response.json()[0]['rates']
    for rate in data:
        ExchangeRate.objects.update_or_create(
            code=rate['code'],
            defaults={'currency': rate['currency'], 'mid': rate['mid']}
        )
    rates = ExchangeRate.objects.all()
    serializer = ExchangeRateSerializer(rates, many=True)
    return JsonResponse({"status": "success", "data": serializer.data})

class ExchangeRateList(generics.ListCreateAPIView):
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRateSerializer
