from django.db import models
from django.forms import CharField


class Client(models.Model):

    name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=6)
    phone_nb = models.IntegerField()
    email = models.CharField(max_length=30)


class Parcel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=6)
    phone_nb = models.IntegerField()
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)