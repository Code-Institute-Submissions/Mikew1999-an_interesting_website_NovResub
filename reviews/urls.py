from django.urls import path
from . import views

urlpatterns = [
    path('<product_id>/', views.review, name='review'),
]
