from rest_framework.generics import ListAPIView, RetrieveAPIView

from core.rest.serializers.transactions import TransactionSerializer
from payment.models import Payment
from restaurant_menu.permissions import IsAdmin


class AdminTransactionListAPIView(ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAdmin]
    queryset = Payment.objects.filter()


class AdminTransactionDetailsAPIView(RetrieveAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAdmin]
    queryset = Payment.objects.filter()
    lookup_field = "id"
