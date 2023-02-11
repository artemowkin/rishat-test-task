from django.urls import path

from . import views


urlpatterns = [
    path('<int:item_id>/', views.get_concrete_item, name='concrete_item')
]