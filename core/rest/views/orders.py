from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView

from core.rest.serializers.orders import AdminOrderSerializer
from order.models import Order
from restaurant_menu.permissions import IsAdmin


class AdminOrderListView(ListAPIView):
    serializer_class = AdminOrderSerializer
    permission_classes = [IsAdmin]
    queryset = Order.objects.filter()


class AdminOrderDetailsView(RetrieveUpdateAPIView):
    serializer_class = AdminOrderSerializer
    permission_classes = [IsAdmin]
    queryset = Order.objects.filter()
    lookup_field = "id"
