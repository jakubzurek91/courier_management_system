from django.urls import path

from cms.views import ParcelView

urlpatterns = [
    path("parcel/list/", ParcelView.as_view(), name='parcel-list'),
]