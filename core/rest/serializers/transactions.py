from rest_framework import serializers

from payment.models import Payment


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
