from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from .services import OrderHandler


async def concrete_order(request: HttpRequest, order_id: int) -> HttpResponse:
    """Возвращает страницу с информацией о конкретном заказе
    
    :param order_id: ID запрашиваемого заказа
    :raises: Http404 если заказ с таким id не найден
    """
    handler = OrderHandler()
    order = await handler.get_concrete(order_id)
    order_items = await handler.get_items(order)
    return render(request, 'orders/concrete.html', {'order': order, 'items': order_items})
