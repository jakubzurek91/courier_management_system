# Create your models here.
from django.db import models
from django.forms import CharField


class Client(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=6)
    phone_nb = models.IntegerField()
    login = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)

    @property
    def client_name(self):
        return f'{self.first_name} {self.last_name}'


class Courier(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_nb = models.IntegerField()


class Parcel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=6)
    phone_nb = models.IntegerField()
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    courier_id = models.ForeignKey(Courier, on_delete=models.CASCADE, null=True)





