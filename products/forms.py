from django.forms import ModelForm
from .models import Products

# Create the form class.


class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ['category', 'title', 'price', 'has_sizes',
                  'description', 'image', 'rate', 'count']
