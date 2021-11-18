''' Imports model form class '''
from django.forms import ModelForm
from .models import DeliveryDetails


class Delivery(ModelForm):
    ''' Defines add product form '''
    class Meta:
        ''' defines form fields '''
        model = DeliveryDetails
        fields = ['address_line_1', 'address_line_2', 'town', 'postcode',
                  'email', 'phone']
