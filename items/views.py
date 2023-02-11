from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from .services import ItemStorage


async def get_concrete_item(request: HttpRequest, item_id: int) -> HttpResponse:
    """Возвращает страницу с конкретным айтемом"""
    storage = ItemStorage()
    item = await storage.get_concrete(item_id)
    return render(request, 'items/concrete.html', {'item': item})
