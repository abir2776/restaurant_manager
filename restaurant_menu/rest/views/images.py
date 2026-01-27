from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from restaurant_menu.models import Image
from restaurant_menu.permissions import IsAdmin
from restaurant_menu.rest.serializers.images import ImageSerializer


class ImageListCreateView(ListCreateAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.filter()

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated(), IsAdmin()]
        return [AllowAny()]


class ImageDetailsView(RetrieveUpdateDestroyAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.filter()
    lookup_field = "id"

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsAuthenticated(), IsAdmin()]
        return [AllowAny()]
