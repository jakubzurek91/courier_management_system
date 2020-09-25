from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, FormView, ListView, UpdateView, DeleteView
from cms.forms import ParcelForm
from cms.models import Parcel, Client
from cms.models import Courier


class ParcelView(LoginRequiredMixin, ListView):
    model = Parcel
    template_name = "parcel_list.html"
    context_object_name = "parcels"


class ParcelFormView(FormView):
    form_class = ParcelForm
    template_name = 'add.html'
    success_url = '/cms/parcel/list'

    def post(self, request):
        print(request.user.get_username())
        client = Client.objects.get(username=request.user.get_username()) #user_ptr_id=3
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


class ParcelUpdateView(UpdateView):
    model = Parcel
    fields = '__all__'
    template_name = "add.html"
    success_url = "../list/"

    def update(self, request):
        form = ParcelForm(request.POST)
        if form.is_valid():
            parcel = Parcel.objects.update(
                name=request.POST['name'],
                address=request.POST['address'],
                zip_code=request.POST['zip_code'],
                phone_nb=request.POST['phone_nb'],
            )


class ParcelDeleteView(DeleteView):
    model = Parcel
    template_name = 'delete_parcel.html'
    success_url = "/cms/parcel/list"


class CourierView(ListView):
    model = Courier
    template_name = "courier/courier_list.html"
    context_object_name = "couriers"


class CourierFormView(CreateView):
    model = Courier
    fields = '__all__'
    template_name = "courier/courier_new.html"
    success_url = "../list/"


class CourierUpdateView(UpdateView):
    model = Courier
    fields = '__all__'
    template_name = "courier/courier_new.html"
    success_url = "../list/"


def HomePage(request):
    return render(request, "home_page.html")