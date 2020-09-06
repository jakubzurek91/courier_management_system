from django import forms

from .models import *


class ParcelForm(forms.ModelForm):
    class Meta:
        model = Parcel
        fields = '__all__'
        exclude = ['id', 'client_id']
