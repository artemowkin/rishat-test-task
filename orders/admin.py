from django.contrib import admin

from .models import Order, Tax, Discount
from .forms import OrderForm, TaxForm, DiscountForm


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    form = OrderForm
    filter_horizontal = ('items', 'taxes', 'discounts')


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    form = TaxForm
    list_display = ('name', 'stripe_id', 'description', 'percentage')


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    form = DiscountForm
    list_display = ('name', 'stripe_id', 'percent_off', 'duration_in_months')
