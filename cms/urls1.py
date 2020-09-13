from django.urls import path

from cms.views import ParcelView, ParcelFormView, HomePage, ParcelUpdateView, ParcelDeleteView

urlpatterns = [
    path("parcel/list/", ParcelView.as_view(), name='parcel-list'),
    path("parcel/add/", ParcelFormView.as_view(), name='parcel_form'),
    path("", HomePage),
    path("parcel/add/<int:pk>", ParcelUpdateView.as_view(), name='update_parcel'),
    path("parcel/<int:pk>/del", ParcelDeleteView.as_view(), name='delete_parcel'),
]