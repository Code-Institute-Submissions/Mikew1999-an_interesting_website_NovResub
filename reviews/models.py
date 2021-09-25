from django.db import models
from django.contrib.auth.models import User
from products.models import Products

class Review(models.Model):
    ''' A model to define the reviews Object '''
    product = models.ForeignKey(Products, null=False, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=False, null=False)
    review_description = models.TextField()
    rating = models.DecimalField(decimal_places=1, max_digits=2, null=False, blank=False)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
