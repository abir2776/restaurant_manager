from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from restaurant_menu.models import OpeningHours
from restaurant_menu.permissions import IsAdmin
from restaurant_menu.rest.serializers.opening_hours import OpeningHoursSerializer


class OpeningHoursListCreateAPIView(ListCreateAPIView):
    serializer_class = OpeningHoursSerializer
    queryset = OpeningHours.objects.filter()

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated(), IsAdmin()]
        return [AllowAny()]


class OpeningHoursDetailsAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OpeningHoursSerializer
    queryset = OpeningHours.objects.filter()
    lookup_field = "id"

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsAuthenticated(), IsAdmin()]
        return [AllowAny()]
