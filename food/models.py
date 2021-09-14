from django.db import models


class Category(models.Model):
    ''' A model to describe the categories of food '''
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    # String method
    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Food(models.Model):
    ''' A model to define the food data '''
    food = models.CharField(max_length=254, blank=False, null=False)
    serving = models.CharField(max_length=100, blank=False, null=False)
    calories = models.CharField(max_length=1000, null=False, blank=False)

    def __str__(self):
        return self.food
