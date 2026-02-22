from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from restaurant_menu.models import Tag
from restaurant_menu.rest.serializers.tags import TagSerializer


class TagListCreateAPIView(ListCreateAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.filter()

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        return [AllowAny()]


class TagDetailsAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.filter()
    lookup_field = "id"

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsAuthenticated()]
        return [AllowAny()]
