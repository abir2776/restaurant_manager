# serializers.py

from rest_framework import serializers

from order.models import CartItem, Order, OrderItem
from order.rest.serializers.address import AddressSerializer
from restaurant_menu.rest.serializers.products import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    total_price = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )

    class Meta:
        model = OrderItem
        fields = ["id", "product", "quantity", "price", "total_price"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
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
            "cart_item_ids",
            "address",
            "payment_type",
        ]
        read_only_fields = [
            "user",
            "total_amount",
            "created_at",
            "updated_at",
            "address",
        ]

    def create(self, validated_data):
        user = self.context["request"].user
        cart_items = CartItem.objects.filter(user=user)

        if not cart_items.exists():
            raise serializers.ValidationError("Cart is empty")

        total_amount = sum(item.total_price for item in cart_items)

        order = Order.objects.create(
            user=user, total_amount=total_amount, **validated_data
        )

        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                price=cart_item.product.price,
            )

        cart_items.delete()

        return order
