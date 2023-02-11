from decimal import Decimal

from django.db import models
from django.urls import reverse


class Currencies(models.TextChoices):
    DOLLARS = 'USD', '$'
    RUBLES = 'RUB', '₽'


class Item(models.Model):
    name: str = models.CharField(max_length=255)
    description: str = models.TextField()
    price: Decimal = models.DecimalField(max_digits=20, decimal_places=2)
    currency = models.CharField(max_length=3, choices=Currencies.choices, default=Currencies.DOLLARS)

    def get_absolute_url(self) -> str:
        return reverse('concrete_item', kwargs={'item_id': self.pk})

    def __str__(self) -> str:
        return f"{self.name}: {self.price}{self.get_currency_display()}"
