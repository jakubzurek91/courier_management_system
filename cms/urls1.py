from django.urls import path

from cms.views import ParcelView, ParcelFormView, HomePage, CourierFormView, ParcelUpdateView, CourierView, \
    CourierUpdateView, ParcelDeleteView

urlpatterns = [
    path("", HomePage),
    path("parcel/list/", ParcelView.as_view(), name='parcel-list'),
    path("parcel/add/", ParcelFormView.as_view(), name='parcel_form'),
    path("parcel/add/<int:pk>", ParcelUpdateView.as_view(), name='update_parcel'),
    path("parcel/<int:pk>/del", ParcelDeleteView.as_view(), name='delete_parcel'),
    path("courier/add/", CourierFormView.as_view(), name='courier_form'),
    path("courier/list/", CourierView.as_view(), name='courier_list'),
    path("courier/list/<int:pk>", CourierUpdateView.as_view(), name='courier_update'),
]