''' Import user model for foreign key '''
from django.contrib.auth.models import User
from django.db import models


class DeliveryDetails(models.Model):
    ''' Stores the delivery Details '''
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL)
    address_line_1 = models.CharField(max_length=254, null=False, blank=False)
    address_line_2 = models.CharField(max_length=254, blank=True)
    town = models.CharField(max_length=254, null=False, blank=False)
    postcode = models.CharField(max_length=10, null=False, blank=False)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return str(self.address_line_1)
