from django.urls import path

from cms.views import ParcelView, ParcelFormView, HomePage

urlpatterns = [
    path("parcel/list/", ParcelView.as_view(), name='parcel-list'),
    path("parcel/add/", ParcelFormView.as_view(), name='parcel_form'),
    path("", HomePage.as_view(), name='home-page'),
]