from django import forms

from .models import *


class ParcelForm(forms.ModelForm):
    class Meta:
        model = Parcel
        fields = '__all__'
        exclude = ['id', 'client_id', 'courier_id', 'status']
        labels = {
            '_id': 'ID',
            'name': 'Adresat',
            'address': 'Adres',
            'zip_code': 'Kod pocztowy',
            'phone_nb': 'Numer telefonu',
            'client_id': 'Użytkownik',
        }

class ParcelUpdateForm(forms.ModelForm):
    class Meta:
        model = Parcel
        exclude = ('courier_id',)

class ParcelStatusForm(forms.ModelForm):
    class Meta:
        model = Parcel
        fields = ['status']