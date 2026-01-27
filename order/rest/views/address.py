from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from order.models import Address
from order.rest.serializers.address import AddressSerializer


class AddressListCreateAPIView(ListCreateAPIView):
    serializer_class = AddressSerializer

    def get_queryset(self):
        user = self.request.user
        addresses = Address.objects.filter(user=user)
        return addresses


class AddressDetailsAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AddressSerializer
    lookup_field = "id"

    def get_queryset(self):
        user = self.request.user
        return Address.objects.filter(user=user)
