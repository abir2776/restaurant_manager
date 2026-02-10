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
    cart_item_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=False,
    )

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
            "cart_item_ids",
        ]
        read_only_fields = [
            "user",
            "total_amount",
            "created_at",
            "updated_at",
            "address",
        ]

    def create(self, validated_data):
        request = self.context["request"]
        user = request.user if request.user.is_authenticated else None
        cart_item_ids = validated_data.pop("cart_item_ids", None)
        if user:
            cart_items = CartItem.objects.filter(user=user)
        else:
            if not cart_item_ids:
                raise serializers.ValidationError(
                    {"cart_item_ids": "This field is required for guest checkout."}
                )
            cart_items = CartItem.objects.filter(id__in=cart_item_ids)

        if not cart_items.exists():
            raise serializers.ValidationError("Cart is empty or invalid cart items")

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
