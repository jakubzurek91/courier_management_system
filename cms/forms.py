from django import forms

from .models import *


class ParcelForm(forms.ModelForm):
    class Meta:
        model = Parcel
        fields = '__all__'
        exclude = ['id', 'client_id']
        labels = {
            '_id': 'ID',
            'name': 'Adresat',
            'address': 'Adres',
            'zip_code': 'Kod pocztowy',
            'phone_nb': 'Numer telefonu',
            'client_id': 'Użytkownik',
        }