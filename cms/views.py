from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, FormView, ListView, UpdateView, DeleteView
from cms.forms import ParcelForm, ParcelUpdateForm, ParcelStatusForm
from cms.models import Parcel, Client, STATUS_CHOICES
from cms.models import Courier
from courier_management_system import settings


class ParcelView(LoginRequiredMixin, ListView):
    model = Parcel
    template_name = "client_parcel_list.html"
    context_object_name = "parcels"
    login_url = settings.LOGIN_URL


class ParcelFormView(FormView):
    form_class = ParcelForm
    template_name = 'add.html'
    success_url = '/cms/parcel/list'

    def post(self, request):
        client = Client.objects.get(username=request.user.get_username())
        form = ParcelForm(request.POST)
        if form.is_valid():
            parcel = Parcel.objects.create(
                name=request.POST['name'],
                address=request.POST['address'],
                zip_code=request.POST['zip_code'],
                phone_nb=request.POST['phone_nb'],
                client_id=client,
                status=0,
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
    fields = ['name', 'address', 'zip_code', 'phone_nb']
    template_name = "update.html"
    success_url = "../list/"

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
    exclude = ['id', 'is_staff', 'is_active', 'date_joined']
    template_name = "courier/courier_new.html"
    success_url = "../list/"


class CourierUpdateView(UpdateView):
    model = Courier
    fields = '__all__'
    template_name = "courier/courier_new.html"
    success_url = "../list/"


def HomePage(request):
    return render(request, "home_page.html")

# def update_parcel_status(request, pk=0):
#     parcel = None
#     if int(pk or 0):
#         parcel = parcel.objects.get(pk=pk)
#
#     if request.method == "POST":
#         parcel.status = request.POST[status]
#         parcel.save()
#     return HttpResponseRedirect('../list/')

class CourierParcelList(LoginRequiredMixin, FormView):
    form_class = ParcelStatusForm
    template_name = "courier_parcel_list.html"
    context_object_name = "parcels"
    success_url = '/cms/parcel/list'
    login_url = settings.LOGIN_URL

    def post(self, request):
        form = ParcelStatusForm(request.POST)
        if form.is_valid():
            parcel = Parcel.objects.update(
                status=request.POST['status'],
            )
            return HttpResponseRedirect('../list/')

    def get(self, request):
        parcels = Parcel.objects.all()
        form = ParcelStatusForm(request.GET)
        return render(request, 'courier_parcel_list.html', {'form': form, 'parcels':parcels})



class ParcelUpdateStatus(UpdateView):
    model = Parcel
    fields = ['status']
    template_name = "set_parcel_status.html"
    success_url = "../list/"

