from decimal import Decimal
from dataclasses import dataclass, field

from pydantic import BaseModel

from items.models import Item
from .models import Order, Tax, Discount


class TaxIn(BaseModel):
    """Схема с данными для создаваемого налога
    
    :param name: Наименование налога
    :param percentage: Процент налога
    :param description: Необязательное описание
    """
    name: str
    percentage: int
    description: str | None = None


class CouponIn(BaseModel):
    """Схема с данными для создаваемого скидочного купона
    
    :param name: Имя купона
    :param percent_off: Процент скидки
    :param duration_in_months: Длительность действия купона в месяцах
    """
    name: str
    percent_off: Decimal
    duration_in_months: int


@dataclass
class BuyingOrder:
    """Схема с полными данными о покупаемом заказе
    
    :param order: Покупаемый заказ
    :param items: Связанные с заказом айтемы
    :param taxes: Связанные с заказом налоги
    :param discounts: Связанные с заказом скидочные купоны
    """
    order: Order
    items: list[Item] = field(default_factory=list)
    taxes: list[Tax] = field(default_factory=list)
    discounts: list[Discount] = field(default_factory=list)
