from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from restaurant_menu.models import Product
from restaurant_menu.permissions import IsAdmin
from restaurant_menu.rest.serializers.products import ProductSerializer


class ProductListCreateAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category__id", "tags__id", "is_popular"]
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "title",
        "category__title",
        "tags__title",
    ]

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated(), IsAdmin()]
        return [AllowAny()]


class ProductDetailsAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter()

    lookup_field = "id"

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsAuthenticated(), IsAdmin()]
        return [AllowAny()]
