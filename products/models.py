from django.db import models


class Category(models.Model):
    ''' A model to describe the categories of food '''
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Products(models.Model):
    '''A model to define the products objcet'''
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=150, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField()
    image = models.URLField(max_length=1024)
    rate = models.DecimalField(max_digits=2, decimal_places=1)
    count = models.PositiveIntegerField()

    def __str__(self):
        return self.title
