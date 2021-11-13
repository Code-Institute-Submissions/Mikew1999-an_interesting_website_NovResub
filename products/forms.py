''' Imports model form class '''
from django.forms import ModelForm
from .models import Products


class ProductForm(ModelForm):
    ''' Defines add product form '''
    class Meta:
        ''' defines form fields '''
        model = Products
        fields = ['category', 'title', 'price', 'has_sizes',
                  'description', 'image', 'rate', 'count']
