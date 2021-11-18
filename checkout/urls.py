from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('delivery_details', views.address, name='delivery_details'),
    path('order_summary', views.order_summary, name='order_summary'),
    path('bank_details', views.bank_details, name='bank_details'),
    path('success', views.success, name='success'),
    path('cancel', views.cancel, name='cancel'),
]
