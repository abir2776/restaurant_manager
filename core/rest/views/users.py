from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
)

from core.choices import UserRole
from core.models import User
from core.rest.serializers.users import AdminUserSerializer
from order.models import Order
from order.rest.serializers.order import OrderSerializer
from restaurant_menu.permissions import IsAdmin, IsSuperUser


class AdminUserListView(ListCreateAPIView):
    serializer_class = AdminUserSerializer
    permission_classes = [IsSuperUser]
    queryset = User.objects.filter(role=UserRole.ADMIN)


class AdminUserDetailsView(RetrieveUpdateDestroyAPIView):
    serializer_class = AdminUserSerializer
    permission_classes = [IsSuperUser]
    queryset = User.objects.filter(role=UserRole.ADMIN)
    lookup_field = "pk"


class AdminUserOrderListView(ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAdmin]

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        queryset = Order.objects.filter(user_id=user_id)
        return queryset


class AdminUserOrderDetailsView(RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAdmin]
    queryset = Order.objects.filter()
    lookup_field = "id"
