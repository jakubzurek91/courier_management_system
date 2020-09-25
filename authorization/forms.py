from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from cms.models import Client, Courier


class RegisterClientForm(forms.ModelForm):
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())
    class Meta:
        model = Client
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'address',
            'zip_code',
            'phone_nb',
        ]

    def clean_login(self):
        login = self.cleaned_data['username']
        if User.objects.filter(username=login).exists():
            raise ValidationError('User with this username already exists.')
        return login

class RegisterCourierForm(forms.ModelForm):
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())
    class Meta:
        model = Courier
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'phone_nb',
        ]

    def clean_login(self):
        login = self.cleaned_data['username']
        if User.objects.filter(username=login).exists():
            raise ValidationError('User with this username already exists.')
        return login


class LoginUserForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())
