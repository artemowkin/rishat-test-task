from django.urls import path

from . import views


urlpatterns = [
    path('<int:order_id>/', views.concrete_order, name='concrete_order')
]