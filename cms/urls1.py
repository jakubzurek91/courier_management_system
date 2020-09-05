from django.urls import path

from cms.views import ParcelView, ParcelCreate, ClientView, ClientCreate

urlpatterns = [
    path('parcels/', ParcelView.as_view(), name='parcel_list'),
    path('new_parcel/', ParcelCreate.as_view(), name='new_parcel'),
    path('clients/', ClientView.as_view(), name='client_list'),
    path('new_client/', ClientCreate.as_view(), name='new_client')
]