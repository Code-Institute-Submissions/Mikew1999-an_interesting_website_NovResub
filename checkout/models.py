from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    ''' A model to define an order '''
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=254, null=False, blank=False)
    address_line_2 = models.CharField(max_length=254, null=True, blank=True)
    town = models.CharField(max_length=70, null=False, blank=False)
    post_code = models.CharField(max_length=8, null=False, blank=False)
    email = models.EmailField(max_length=254, blank=False, null=False)
    phone = models.IntegerField(null=True, blank=True)
    delivery_cost = models.CharField(max_length=100, null=False, blank=False)
    total = models.CharField(max_length=10000, null=False, blank=False)
    items = models.CharField(max_length=100, null=False, blank=False)
