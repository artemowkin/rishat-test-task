from django.forms import ModelForm
from django.core.exceptions import ValidationError

from .models import Item


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'currency')

    def clean_currency(self):
        new_currency = self.cleaned_data['currency']
        if self.instance.pk:
            if new_currency != self.instance.currency:
                raise ValidationError('You can not change item currency')

        return new_currency