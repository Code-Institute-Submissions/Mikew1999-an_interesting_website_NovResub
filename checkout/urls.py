from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('order_summary', views.order_summary, name='order_summary'),
    path('bank_details', views.bank_details, name='bank_details'),
]
