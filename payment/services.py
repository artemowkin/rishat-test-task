import stripe

from test_task.config import config
from items.models import Item
from orders.models import Tax
from orders.schemas import TaxIn, CouponIn, BuyingOrder


class Payment:
    """Класс, инкапсулирующий логику взаимодействия с платежной системой"""

    def __init__(self):
        self._api_key = config.stripe_key
        stripe.api_key = config.stripe_key

    def _get_keypair_for_item(self, item: Item, taxes: list[Tax] | None = None) -> dict:
        """Создает keypari для покупаемого айтема
        
        :param item: Запись покупаемого айтема из БД
        :param taxes: Налоги на товар
        :returns: Словарь с данными о товаре для платежной системы stripe
        """
        return {
            'price_data': {
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
                'currency': item.currency,
                'unit_amount': int(float(item.price) * 100),
            },
            'tax_rates': [tax.stripe_id for tax in taxes] if taxes else [],
            'quantity': 1
        }

    def buy_item(self, item: Item, success_url: str) -> str:
        """Купить конкретный айтем
        
        :param item: Запись айтема из БД
        :param success_url: URL, на который будет происходить редирект после оплаты
        :returns: ID checkout сессии
        """
        item_keypair = self._get_keypair_for_item(item)
        session = stripe.checkout.Session.create(
            success_url=success_url,
            line_items=[item_keypair],
            mode='payment'
        )
        return session['id']

    def buy_order(self, buying_order: BuyingOrder, success_url: str) -> str:
        """Купить заказ (с несколькими айтемами)
        
        :param buying_order: покупаемый заказ с информацией о самом заказе,
            прикрепленными айтемами, налогами и скидками
        :param success_url: URL, на который будет происходить редирект после оплаты
        :returns: ID checkout сессии
        """
        items_keypairs = [
            self._get_keypair_for_item(item, buying_order.taxes) for item in buying_order.items
        ]
        discounts = [{'coupon': discount.stripe_id} for discount in buying_order.discounts]
        session = stripe.checkout.Session.create(
            success_url=success_url,
            line_items=items_keypairs,
            mode='payment',
            discounts=discounts
        )
        return session['id']

    def create_tax(self, tax: TaxIn) -> str:
        """Создает налог в Stripe
        
        :param tax: Данные о налоге
        :returns: ID созданного налога
        """
        tax_data = {
            'display_name': tax.name,
            'inclusive': False,
            'percentage': tax.percentage,
            'description': tax.description or None
        }
        tax_data = {k: v for k, v in tax_data.items() if v is not None}
        tax = stripe.TaxRate.create(**tax_data)
        return tax['id']

    def create_coupon(self, coupon: CouponIn) -> str:
        """Создает купон на скидку в Stripe
        
        :param coupon: Данные о купоне
        :returns: ID созданного купона
        """
        coupon = stripe.Coupon.create(
            duration='repeating',
            duration_in_months=coupon.duration_in_months,
            percent_off=coupon.percent_off,
            name=coupon.name
        )
        return coupon['id']
