''' Required django import '''
from django.contrib.auth.models import User
from django.db import models


# models inspired from code institute walkthrough project
class Category(models.Model):
    ''' A model to describe the categories of products '''
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        ''' String method '''
        return str(self.name)

    def get_friendly_name(self):
        ''' Returns the friendly name of category '''
        return self.friendly_name


class Products(models.Model):
    '''A model to define the products object'''
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=150, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    has_sizes = models.BooleanField(default=False, blank=True, null=True)
    description = models.TextField()
    image = models.URLField(max_length=1024, null=True, blank=True)
    rate = models.DecimalField(
        max_digits=2, decimal_places=1, blank=True, null=True, default=0)
    count = models.PositiveIntegerField(blank=True, null=True, default=0)
    author = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        ''' Returns string of title '''
        return str(self.title)


class Likes(models.Model):
    ''' A Model to define a like '''
    product = models.ForeignKey(
        'Products', null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product)
