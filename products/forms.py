from django.forms import ModelForm
from .models import Products


class ProductForm(ModelForm):
    model = Products
    fields = ['title', 'price', 'has_sizes', 'description', 'image']
