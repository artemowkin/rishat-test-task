from django.http.request import HttpRequest
from django.http.response import JsonResponse

from items.services import ItemStorage
from orders.services import get_order_with_all_payment_data
from .services import Payment


async def buy_item(request: HttpRequest, item_id: int) -> JsonResponse:
    """Купить конкретный айтем
    
    :param item_id: ID покупаемого айтема
    :raises: Http404 если айтема с таким ID не найдено
    :returns: ID checkout сессии
    """
    payment = Payment()
    item_storage = ItemStorage()
    item = await item_storage.get_concrete(item_id)
    session_id = payment.buy_item(item, request.build_absolute_uri(item.get_absolute_url()))
    return JsonResponse({'session_id': session_id})


async def buy_order(request: HttpRequest, order_id: int) -> JsonResponse:
    """Купить заказ с несколькими товарами
    
    :param order_id: ID заказа
    :raises: Http404 если заказа с таким ID не найдено
    :returns: ID checkout сессии
    """
    payment = Payment()
    buying_order = await get_order_with_all_payment_data(order_id)
    session_id = payment.buy_order(buying_order, request.build_absolute_uri('/'))
    return JsonResponse({'session_id': session_id})
