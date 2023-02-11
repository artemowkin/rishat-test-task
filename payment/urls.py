from django.urls import path

from . import views


urlpatterns = [
    path('item/<int:item_id>/', views.buy_item, name='buy_item'),
    path('order/<int:order_id>/', views.buy_order, name='buy_order'),
]
