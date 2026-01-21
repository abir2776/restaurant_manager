# views.py

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from order.models import CartItem
from rest_framework.exceptions import ValidationError
from order.rest.serializers.cart import CartItemSerializer


class CartItemListCreateView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        cart_ids = self.request.query_params.get("cart_ids")

        if not cart_ids:
            raise ValidationError({"cart_ids": "This query parameter is required."})

        try:
            cart_ids = [int(cid) for cid in cart_ids.split(",")]
        except ValueError:
            raise ValidationError(
                {"cart_ids": "cart_ids must be a comma-separated list of integers."}
            )

        return CartItem.objects.filter(id__in=cart_ids)

class CartItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return CartItem.objects.filter()
