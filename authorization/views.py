from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

from authorization.forms import RegisterClientForm, LoginUserForm, RegisterCourierForm
from cms.models import Client, Courier


def client_register_view(request):

    form = RegisterClientForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = Client.objects.create(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                address=form.cleaned_data['address'],
                zip_code=form.cleaned_data['zip_code'],
                phone_nb=form.cleaned_data['phone_nb'],
            )

            user.set_password(form.cleaned_data['password'])
            user.save()
            group = Group.objects.get(name='clients')  # must be created before used, create through django admin
            user.groups.add(group)
            messages.add_message(request, messages.SUCCESS, f"Welcome {form.cleaned_data['username']}!!")

    return render(
        request,
        'register.html',
        context={'form': form}
    )

def courier_register_view(request):

    form = RegisterCourierForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = Courier.objects.create(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                phone_nb=form.cleaned_data['phone_nb'],
            )

            user.set_password(form.cleaned_data['password'])
            user.save()
            group = Group.objects.get(name='couriers')  # must be created before used, create through django admin
            user.groups.add(group)
            messages.add_message(request, messages.SUCCESS, f"Welcome {form.cleaned_data['username']}!!")

    return render(
        request,
        'register.html',
        context={'form': form}
    )


def login_view(request):

    form = LoginUserForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user_login = form.cleaned_data['username']
            user = authenticate(username=user_login, password=form.cleaned_data['password'])
            if user:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, f'Successfully logged in {user_login}!')

    return render (
        request,
        'login.html',
        context={'form': form}
    )


def logout_view(request):
    logout(request)

    return redirect(login_view)
