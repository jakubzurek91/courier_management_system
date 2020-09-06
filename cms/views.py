from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, FormView, ListView

from cms.forms import ParcelForm
from cms.models import Parcel


class ParcelView(ListView):
    model = Parcel
    template_name = "parcel_list.html"
    context_object_name = "parcels"


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ParcelForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ParcelForm()

    return render(request, 'add.html', {'form': form})

def parcel_list(request):
    parcels = Parcel.objects.all()

    return render(request, "parcel_list.html", {
        "parcels": parcels
    })