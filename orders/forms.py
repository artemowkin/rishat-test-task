from django.forms import ModelForm
from django.core.exceptions import ValidationError

from payment.services import Payment
from .models import Order, Tax, Discount
from .schemas import TaxIn, CouponIn


class OrderForm(ModelForm):
    """
    Форма для создания заказа. Нужна для валидации валют
    айтемов в заказе: все айтемы должны быть одной валюты
    """

    class Meta:
        model = Order
        fields = ('items', 'taxes', 'discounts')

    def clean_items(self):
        """
        Проверяет, одинакова ли валюта для всех выбранных айтемов.
        Если нет, то выдает ошибку
        """
        data = self.cleaned_data['items']
        first_currency = data[0].currency
        for item in data:
            if item.currency != first_currency:
                raise ValidationError("Items in order must be with the same currency")

        return data


class TaxForm(ModelForm):
    """
    Форма для создания налога. Нужна для создания налога в
    платежной системе перед сохранением в БД (для сохранения ID налога)
    """

    class Meta:
        model = Tax
        fields = ['name', 'percentage', 'description']

    def save(self, *args, **kwargs):
        """
        Создает налог в платежной системе и сохраняет в поле `stripe_id`
        его идентификатор
        """
        tax = TaxIn(**self.cleaned_data)
        payment = Payment()
        tax_id = payment.create_tax(tax)
        self.instance.stripe_id = tax_id
        return super().save(*args, **kwargs)


class DiscountForm(ModelForm):
    """
    Форма для создания скидочного купона. Нужна для создания купона в
    платежной системе перед сохранением в БД (для сохранения ID купона)
    """

    class Meta:
        model = Discount
        fields = ['name', 'percent_off', 'duration_in_months']

    def save(self, *args, **kwargs):
        """
        Создает скидочный купон в платежной системе и сохраняет в поле `stripe_id`
        его идентификатор
        """
        coupon = CouponIn(**self.cleaned_data)
        payment = Payment()
        coupon_id = payment.create_coupon(coupon)
        self.instance.stripe_id = coupon_id
        return super().save(*args, **kwargs)
