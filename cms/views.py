from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, FormView, ListView

from cms.forms import ParcelForm
from cms.models import Parcel, Client


class HomePage(ListView):
    template_name = "home_page.html"

class ParcelView(ListView):
    model = Parcel
    template_name = "parcel_list.html"
    context_object_name = "parcels"

class ParcelFormView(FormView):
    form_class = ParcelForm
    template_name = 'add.html'
    success_url = '/cms/parcel/list'

    def post(self, request):
        client = Client.objects.get()
        form = ParcelForm(request.POST)
        if form.is_valid():
            parcel = Parcel.objects.create(
                name=request.POST['name'],
                address=request.POST['address'],
                zip_code=request.POST['zip_code'],
                phone_nb=request.POST['phone_nb'],
                client_id=client
            )
            return HttpResponseRedirect('../list/')
        else:
            form = ParcelForm()
            return render(request, 'add.html', {'form': form})

    def get(self, request):
        form = ParcelForm()
        return render(request, 'add.html', {'form': form})


def parcel_list(request):
    parcels = Parcel.objects.all()

    return render(request, "parcel_list.html", {
        "parcels": parcels
    })