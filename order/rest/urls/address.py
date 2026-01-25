from django.urls import path

from order.rest.views.address import AddressDetailsAPIView, AddressListCreateAPIView

urlpatterns = [
    path("", AddressListCreateAPIView.as_view(), name="address-list-create"),
    path("<int:id>", AddressDetailsAPIView.as_view(), name="address-details"),
]
