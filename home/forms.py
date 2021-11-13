''' Django import '''
from django.forms import ModelForm
from .models import ContactMe


class ContactMeForm(ModelForm):
    ''' Defines contact me form '''
    class Meta:
        ''' Defines form fields '''
        model = ContactMe
        fields = ['name', 'email', 'message']
