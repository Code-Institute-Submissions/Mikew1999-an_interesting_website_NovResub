from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('<product_id>', views.productdetails, name='productdetails'),
    path('add_product', views.add_product, name='add_product'),
]
