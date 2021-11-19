''' Import user model for foreign key '''
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Order(models.Model):
    ''' Defines an order '''
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL)
    address_line_1 = models.CharField(max_length=254, null=False, blank=False)
    address_line_2 = models.CharField(max_length=254, blank=True)
    town = models.CharField(max_length=254, null=False, blank=False)
    postcode = models.CharField(max_length=10, null=False, blank=False)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    items = ArrayField(models.CharField(max_length=3000), default='')
