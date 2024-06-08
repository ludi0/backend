from django.db import models


class ExchangeRate(models.Model):
    currency = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    mid = models.DecimalField(max_digits=10, decimal_places=2)
