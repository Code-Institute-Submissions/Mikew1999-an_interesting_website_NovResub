from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('bank_details', views.bank_details, name='bank_details'),
]