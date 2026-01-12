# views.py

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from order.models import CartItem
from order.rest.serializers.cart import CartItemSerializer


class CartItemListCreateView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == "POST":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)


class CartItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)
