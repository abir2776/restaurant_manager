# serializers.py

from rest_framework import serializers

from order.models import Order, OrderItem
from order.rest.serializers.address import AddressSerializer
from restaurant_menu.rest.serializers.products import ProductSerializer


class AdminOrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    total_price = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )

    class Meta:
        model = OrderItem
        fields = ["id", "product", "quantity", "price", "total_price"]


class AdminOrderSerializer(serializers.ModelSerializer):
    items = AdminOrderItemSerializer(many=True, read_only=True)
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "user",
            "status",
            "total_amount",
            "items",
            "created_at",
            "updated_at",
            "address",
            "payment_type",
            "cancelled_reason"
        ]
        read_only_fields = [
            "id",
            "user",
            "total_amount",
            "items",
            "created_at",
            "updated_at",
            "address",
            "payment_type",
        ]

    def validate(self, attrs):
        status = attrs.get("status")
        cancelled_reason = attrs.get("cancelled_reason")

        if status == "cancelled" and (
            not cancelled_reason or len(cancelled_reason) <= 0
        ):
            raise serializers.ValidationError(
                {
                    "cancelled_reason": "Cancelled reason is required when status is cancelled."
                }
            )

        return attrs
