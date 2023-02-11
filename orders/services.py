from django.http import Http404

from items.models import Item
from .models import Order, Tax, Discount
from .schemas import BuyingOrder


class OrderHandler:
    """Класс, инкапсулирующий логику работы с заказами"""

    async def get_concrete(self, order_id: int) -> Order:
        """Возвращает конкретный заказ по его ID
        
        :param order_id: ID получаемого заказа
        :raises: Http404 если заказ с таким ID не найден
        :returns: Полученный заказ
        """
        try:
            return await Order.objects.aget(pk=order_id)
        except Order.DoesNotExist:
            raise Http404

    async def get_items(self, order: Order) -> list[Item]:
        """Получает айтемы, прикрепленные к заказу
        
        :param order: Заказ, для которого получаются прикрепленные айтемы
        :returns: Прикрепленные айтемы
        """
        orders = [item async for item in order.items.all()]
        return orders

    async def get_taxes(self, order: Order) -> list[Tax]:
        """Получает налоги, прикрепленные к заказу
        
        :param order: Заказ, для которого получаются прикрепленные налоги
        :returns: Прикрепленные налоги
        """
        taxes = [tax async for tax in order.taxes.all()]
        return taxes

    async def get_discounts(self, order: Order) -> list[Discount]:
        """Получает скидочные купоны, прикрепленные к заказу
        
        :param order: Заказ, для которого получаются прикрепленные купоны
        :returns: Прикрепленные купоны
        """
        discounts = [discount async for discount in order.discounts.all()]
        return discounts


async def get_order_with_all_payment_data(order_id: int) -> BuyingOrder:
    """Возвращает заказ с полными данными для заказа
    (прикрепленные айтемы, налоги, скидочные купоны)
    
    :param order_id: ID получаемого заказа
    :raises: Http404 если заказа с таким ID не существует
    :returns: Полные данные о заказе
    """
    handler = OrderHandler()
    order = await handler.get_concrete(order_id)
    items = await handler.get_items(order)
    taxes = await handler.get_taxes(order)
    discounts = await handler.get_discounts(order)
    return BuyingOrder(order=order, items=items, taxes=taxes, discounts=discounts)
