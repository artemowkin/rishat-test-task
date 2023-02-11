from django.contrib import admin

from .models import Item
from .forms import ItemForm


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'currency')
    search_fields = ('name',)
    form = ItemForm
