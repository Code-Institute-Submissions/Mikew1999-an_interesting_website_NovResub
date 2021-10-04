from django.forms import ModelForm
from .models import AddressDetails


class ProductForm(ModelForm):
    class Meta:
        model = AddressDetails
        fields = ['address_line_1', 'address_line_2', 'town', 'post_code',
                  'email', 'phone']
