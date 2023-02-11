from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path('items/', include('items.urls')),
    path('orders/', include('orders.urls')),
    path('buy/', include('payment.urls')),
]
