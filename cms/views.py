from django.views.generic import ListView, CreateView

from cms.models import Parcel, Client


class ParcelView(ListView):
    model = Parcel
    template_name = "parcel/parcel_list.html"
    context_object_name = "parcels"


class ParcelCreate(CreateView):
    model = Parcel
    fields = '__all__'
    template_name = "parcel/new_parcel.html"
    success_url = "/cml/list/"


class ClientView(ListView):
    model = Client
    template_name = "client/client_list.html"
    context_object_name = "clients"


class ClientCreate(CreateView):
    model = Client
    fields = "__all__"
    template_name = "client/new_client.html"
    success_url = "/cms/clients/"



