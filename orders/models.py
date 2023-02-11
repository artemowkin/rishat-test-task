from decimal import Decimal

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

from items.models import Item


class Tax(models.Model):
    stripe_id: str = models.CharField(max_length=500, editable=False)
    name: str = models.CharField(max_length=255)
    description: str | None = models.CharField(max_length=500, blank=True)
    percentage: int = models.PositiveIntegerField(validators=[
        MinValueValidator(0), MaxValueValidator(100)
    ])

    def __str__(self) -> str:
        return self.name


class Discount(models.Model):
    stripe_id: str = models.CharField(max_length=500, null=True, editable=False)
    name: str = models.CharField(max_length=100)
    percent_off: Decimal = models.DecimalField(max_digits=5, decimal_places=2, validators=[
        MinValueValidator(0), MaxValueValidator(75)
    ])
    duration_in_months: int = models.PositiveIntegerField(validators=[
        MinValueValidator(1)
    ])

    def __str__(self) -> str:
        return f"{self.name} (-{self.percent_off}%)"


class Order(models.Model):
    items = models.ManyToManyField(Item)
    taxes = models.ManyToManyField(Tax, blank=True)
    discounts = models.ManyToManyField(Discount, blank=True)

    def get_absolute_url(self) -> str:
        return reverse('concrete_order', kwargs={'order_id': self.pk})

    def __str__(self) -> str:
        return f"Order {self.pk}"
