from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping_bag, name='shopping_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('remove/<item_id>/', views.remove_item, name='remove_item'),
    path('amend_bag/<item_id>/', views.amend_bag, name='amend_bag'),
]
