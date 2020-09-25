# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Client(User):
    address = models.CharField(max_length=30,null=True)
    zip_code = models.CharField(max_length=6,null=True)
    phone_nb = models.IntegerField(null=True)

    @property
    def client_name(self):
        return f'{self.first_name} {self.last_name}'


class Courier(User):
    phone_nb = models.IntegerField()

    @property
    def courier_name(self):
        return f'{self.first_name} {self.last_name}'


class Parcel(models.Model):
    _id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=6)
    phone_nb = models.IntegerField()
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    courier_id = models.ForeignKey(Courier, on_delete=models.CASCADE, null=True)