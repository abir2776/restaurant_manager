from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView

from core.rest.serializers.orders import AdminOrderSerializer
from order.models import Order
from restaurant_menu.permissions import IsAdmin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class AdminOrderListView(ListAPIView):
    serializer_class = AdminOrderSerializer
    permission_classes = [IsAdmin]
    queryset = Order.objects.filter()
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ["id", "payment_id", "user__first_name", "user__last_name"]
    filterset_fields = ["status"]


class AdminOrderDetailsView(RetrieveUpdateAPIView):
    serializer_class = AdminOrderSerializer
    permission_classes = [IsAdmin]
    queryset = Order.objects.filter()
    lookup_field = "id"
