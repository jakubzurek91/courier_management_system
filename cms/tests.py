import os
from http import HTTPStatus

from django.test import TestCase

# Create your tests here.
from cms.models import Parcel, Client, Courier


class ParcelViewTestCase(TestCase):
    def setUp(self):
        pass
        for i in range(10):
            Client.objects.create_user(
                username='gruba'+str(i),
                password='124wqag4f',
                email='alfred@gmail'+str(i)+'.com',
                first_name='Edek',
                last_name='Edek',
                address='Nadwodna',
                zip_code='06-100',
                phone_nb='500555444',
            )

        courier = Courier.objects.create_user(
            username='gruby',
            password='124wqag4f',
            email='alfred@gmail.com',
            first_name='Edek',
            last_name='Edek',
            phone_nb='500555444',
        )

        Parcel.objects.create(
            name='gruby',
            address='Nadwodna',
            zip_code = '06-100',
            phone_nb = '500555444',
            client_id = Client.objects.get(username='gruba0'),
            courier_id = Courier.objects.get(username='gruby'),
            status = 0,
        )

    def test_get(self):
        login = self.client.login(username='gruba0', password='124wqag4f')
        response = self.client.get("http://127.0.0.1:8000/cms/gruba/parcel/list/")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        # self.assertContains(response, "<h1>Add Book</h1>", html=True)