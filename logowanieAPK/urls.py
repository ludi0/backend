from django.urls import path
from .views import fetch_exchange_rates, ExchangeRateList

urlpatterns = [
    path('fetch-exchange-rates/', fetch_exchange_rates, name='fetch-exchange-rates'),
    path('api/exchange-rates/', ExchangeRateList.as_view(), name='exchange-rates'),
]
