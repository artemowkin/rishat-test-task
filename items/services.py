from django.http import Http404

from .models import Item


class ItemStorage:
    """Хранилище для айтемов с логикой взаимодействия с ними"""

    async def get_concrete(self, pk: int) -> Item:
        """Возвращает конкретный айтем по его primary key
        
        :param pk: Primary key айтема
        :raises: Http404
        :returns: Полученный айтем
        """
        try:
            return await Item.objects.aget(pk=pk)
        except Item.DoesNotExist:
            raise Http404
