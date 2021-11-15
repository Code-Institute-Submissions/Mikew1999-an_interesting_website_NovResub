''' Required django import '''
from django.db import models


class ContactMe(models.Model):
    ''' Defines the contact me table '''
    name = models.CharField(max_length=254)
    email = models.EmailField(blank=False, null=False)
    message = models.TextField(max_length=10000, blank=False)

    def __str__(self):
        ''' Returns string of name '''
        return str(self.name)


class Newsletter(models.Model):
    ''' Defines the newsletter table '''
    email = models.EmailField(blank=False, null=False)

    def __str__(self):
        return str(self.email)
